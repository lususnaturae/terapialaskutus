# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db.models import Sum, Max, Min
import datetime
from django.db import models
from django.core.urlresolvers import reverse
from therapyinvoicing.customers.models import TimeStampedModel, CompanyProfileModel, SessionModel, CustomerModel
from therapyinvoicing.customers.models import Customer, Session, CompanyProfile
from ..api.tasks import update_api_monthlyrevenue
from django.shortcuts import get_object_or_404


class InvoiceCustomer(CustomerModel):
    """
        Used to store copy of Customer.
        Due to data in Invoice must not be changed after invoice has been sent
        Link to original Customer will be created
    """
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.lastName + ", " + self.firstName


class InvoiceCompanyProfile(CompanyProfileModel):
    """
        Used to store copy of CompanyProfile.
        Due to data in Invoice must not be changed after invoice has been sent
        Link to original Customer will be created
    """
    companyProfile = models.ForeignKey(CompanyProfile)

    def __str__(self):
        return self.companyName


class Invoice(TimeStampedModel):
    """

    """

    invoiceCustomer = models.ForeignKey(InvoiceCustomer)
    invoiceCompanyProfile = models.ForeignKey(InvoiceCompanyProfile)
    date = models.DateField(null=True)
    invoiceNumber = models.PositiveIntegerField(default=1000)
    paidDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('customerinvoicing:invoice_detail', args=[str(self.id)])

# allow views to automatically send user to the detail view of the object after creating or updating object
    def create_invoices(*args, **kwargs):
        """
            Copy Customers into InvoiceCustomer with sessions that has not been invoiced
            Copy is needed to keep invoice customer data from changing after invoice has been created

        """
        #create copy of Customer with reference to original
        cp = CompanyProfile.objects.all()[:1].get()
        companycopy = InvoiceCompanyProfile(

                companyProfile = cp,
                companyName = cp.companyName,
                firstName = cp.firstName,
                additionalName = cp.additionalName,
                lastName = cp.lastName,
                address = cp.address,
                zipCode = cp.zipCode,
                city = cp.city,
                telephone = cp.telephone,
                email = cp.email,
                vatId = cp.vatId,
                iban = cp.iban,
                bic = cp.bic,
                serviceproviderType = cp.serviceproviderType,
                invoiceRefType = cp.invoiceRefType,
                taxAdvanceType = cp.taxAdvanceType

            )
        companycopy.save()

        # Get Customers that have sessions that has not been invoiced
        # Create kelainvoice
        invoicablesessions = Session.objects.filter(sessionDone=True, customerInvoiced=False)
        for cc in invoicablesessions.values('customer').distinct():
            # Copy Customer to KelaInvoiceCustomer
            ccobj = get_object_or_404(Customer, pk=cc['customer'])

            # create copy of Customer with reference to original
            customercopy = InvoiceCustomer(

                customer = ccobj,
                firstName = ccobj.firstName,
                additionalName = ccobj.additionalName,
                lastName = ccobj.lastName,
                address = ccobj.address,
                zipCode = ccobj.zipCode,
                city = ccobj.city,
                country = ccobj.country,
                ssn = ccobj.ssn,
                telephone = ccobj.telephone,
                email = ccobj.email,
                status = ccobj.status,
                sessionprice = ccobj.sessionprice,
                therapyCategory = ccobj.therapyCategory,
                sessionpriceKelaRefund = ccobj.sessionpriceKelaRefund,
                # statementpriceKela = ccobj.statementpriceKela

            )
            customercopy.save()


            # find max invoicenumber
            invlist = Invoice.objects.all().order_by('invoiceNumber')
            if invlist:
                invagg = invlist.aggregate(max_invoicenumber = Max('invoiceNumber'))
                maxnum = invagg['max_invoicenumber']
            else:
                # if no invoices set max number to 140
                maxnum = 140
            # Create Invoice for customer
            invoice = Invoice(
                invoiceCustomer = customercopy,
                invoiceCompanyProfile= companycopy,
                date = datetime.datetime.now(),
                invoiceNumber = maxnum + 1
            )
            invoice.save()

            # Select customers therapy sessions and create copy KelaInvoiceLineItem
            # Reference to original Session included
            ccsessions = Session.objects.filter(customer=ccobj, sessionDone=True, customerInvoiced=False)
            for ss in ccsessions:
                sic = InvoiceLineItem(
                    date = ss.date,
                    time = ss.time,
                    sessionInvoiceType = ss.sessionInvoiceType,
                    kelaInvoiceType = ss.kelaInvoiceType,
                    sessionType = ss.sessionType,
                    sessionDone = ss.sessionDone,
                    kelaInvoiced = ss.kelaInvoiced,
                    customerInvoiced = ss.customerInvoiced,
                    invoice = invoice,
                    session = ss,
                    sessionprice = ss.sessionprice,
                    sessionpriceKelaRefund = ss.sessionpriceKelaRefund
                )
                sic.save()
        # set customerInvoiced status to True
        for i in invoicablesessions:
            i.customerInvoiced = True
            i.save()
        # update monthlyrevenue table at api module
        update_api_monthlyrevenue()



    def get_customerinvoicablesessions(*args, **kwargs):
        """
           Finds all sessions that has been completed (sessionDone=True) and are not invoiced from Kela (kelaInvoiced=False)

        :return:
        [{'invoicablesessions': [<Session: 2016-02-17>],
         'additionalName': '',
          'lastName': 'Asiakas',
           'kelaRefundTotal': Decimal('57.60'),
            'id': 2,
             'firstName': 'Anne'}
             ...
        ]
        """
        #Find customers that has session that are not invoiced from Kela
        invoicablecustomers = Session.objects.filter(sessionDone=True, customerInvoiced=False).values('customer').distinct()
        rlist = []

        for i in invoicablecustomers:
            icobj = get_object_or_404(Customer, id=i['customer'])
            if icobj:
                # Find Sessions of this Customer sorted by 'date'
                slist = Session.objects.filter(sessionDone=True, customerInvoiced=False, customer=icobj).order_by('date')
                sagg = slist.aggregate(kelaRefundTotal = Sum('sessionpriceKelaRefund'), max_date = Max('date'), min_date = Min('date'))
                rlist.append({
                    'id': icobj.id,
                    'firstName': icobj.firstName,
                    'lastName': icobj.lastName,
                    'additionalName': icobj.additionalName,
                    'invoicablesessions': slist,
                    'kelaRefundTotal': sagg['kelaRefundTotal']
                })
        return rlist


class InvoiceLineItem(SessionModel):
    """
        Used to store copy of Session
        Link to original Session will be created
    """
    invoice = models.ForeignKey(Invoice)
    session = models.ForeignKey(Session)


    def __str__(self):
        return str(self.date) + " " + str(self.time)

    def get_invoicelineitems(*args, **kwargs):
        """
        Finds all invoicelinelineitems
        :param kwargs: pk of Invoice object
        :return:
        e.g.
        {'invoiceTotal': Decimal('22.40'),
         'invoiceTotalWithoutKelaRefund': Decimal('80.00'),
         'kelaRefundTotal': Decimal('57.60'),
         'invoicelineitems': [
           {'kelaInvoiceType': 'CANINVOICEKELA',
            'sessionType': 'Yksilöterapia',
            'sessionpriceKelaRefund': Decimal('57.60'),
            'date': datetime.date(2016, 2, 10),
            'sessionInvoiceType': 'SINGLESESSION',
            'sessionprice': Decimal('80.00')}
            ...
            ]
        }
        """
        ki = get_object_or_404(Invoice, id=kwargs['pk'])
        kili = InvoiceLineItem.objects.filter(invoice=ki).order_by('date')
        iline = []
        kelarefund = 0
        pricewithoutkelarefund = 0
        totalprice = 0
        #convert choices list to dictionary
        sessiontypechoices = dict(Session.SESSION_TYPE_CHOICES)

        for icobj in kili:
            iline.append({
                'date': icobj.date,
                'sessionInvoiceType': icobj.sessionInvoiceType,
                'kelaInvoiceType': icobj.kelaInvoiceType,
                'sessionType': sessiontypechoices[icobj.sessionType],
                'sessionprice': icobj.sessionprice,
                'sessionpriceKelaRefund': icobj.sessionpriceKelaRefund
            })
            kelarefund += icobj.sessionpriceKelaRefund
            pricewithoutkelarefund += icobj.sessionprice
            totalprice += (icobj.sessionprice - icobj.sessionpriceKelaRefund)

        return {
            'invoicelineitems': iline,

            'kelaRefundTotal': kelarefund,
            'invoiceTotal': totalprice,
            'invoiceTotalWithoutKelaRefund': pricewithoutkelarefund
        }
