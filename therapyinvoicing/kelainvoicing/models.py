# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db.models import Sum, Max, Min
import datetime
from django.db import models
from django.core.urlresolvers import reverse
from therapyinvoicing.customers.models import TimeStampedModel, CompanyProfileModel, SessionModel, CustomerModel
from therapyinvoicing.customers.models import Customer, Session, CompanyProfile
from django.shortcuts import get_object_or_404
from ..api.tasks import update_api_monthlyrevenue


class KelaContactProfile(TimeStampedModel):
    """
         KELA invoice address and primpary contact
    """
    legalName = models.CharField(max_length=120)
    firstName = models.CharField(max_length=120, blank=True)
    additionalName = models.CharField(max_length=120, blank=True)
    lastName = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120)
    zipCode = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True)
    telephone = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.legalName

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('kelainvoicing:kelacontactprofile_update', args=[str(self.id)])

    def get_or_create_kelacontactprofile(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if KelaContactProfile.objects.all().exists():
            cp = KelaContactProfile.objects.all()[:1].get()
        else:
            cp = KelaContactProfile(
                legalName = 'KELA',
                firstName = '',
                additionalName = '',
                lastName = '',
                address = 'PL 577',
                zipCode = '33101',
                city = 'TAMPERE',
                country = 'Finland',
                telephone = '',
                email = ''
            )
            cp.save()
        return cp




class KelaStatement(CompanyProfileModel):
    """
        KelaStatement
    """

    date = models.DateField()
    #incremental number if InvoiceRefType = 'TILITYSNUMERO'
    orderno = models.CharField(max_length=120, blank=True, editable=True)
    #manually filled if InvoiceRefType = 'VIITENUMERO'
    invoiceRef = models.CharField(max_length=120, blank=True, editable=True)
    taxAdvanceExplanation = models.CharField(max_length=120, blank=True, editable=True)

    def create_kelainvoices(*args, **kwargs):
        """
            Copy Customers into KelaInvoiceCustomer with sessions that has not been invoiced
            Copy is needed to keep invoice customer data from changing after invoice has been created
        :return:
        """



        # Get all Sessions that can be invoiced

        ksobj = get_object_or_404(KelaStatement, pk=kwargs['pk'])
        #create copy of Customer with reference to original
        #TODO: Add error management. If does not exist raises DoesNotExist
        cp = CompanyProfile.objects.all()[:1].get()
        companycopy = KelaInvoiceCompanyProfile(

                companyProfile = cp,
                companyName = cp.companyName,
                kelaStatement= ksobj,
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
        invoicablesessions = Session.objects.filter(sessionDone=True, kelaInvoiced=False)
        for cc in invoicablesessions.values('customer').distinct():
            # Copy Customer to KelaInvoiceCustomer
            ccobj = get_object_or_404(Customer, pk=cc['customer'])

            #create copy of Customer with reference to original
            customercopy = KelaInvoiceCustomer(

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

            # Create KelaInvoice for customer
            invoice = KelaInvoice(
                kelaInvoiceCustomer = customercopy,
                kelaStatement= ksobj,
                date = datetime.datetime.now()


            )
            invoice.save()

            # Select customers therapy sessions and create copy KelaInvoiceLineItem
            # Reference to original Session included
            ccsessions = Session.objects.filter(customer=ccobj, sessionDone=True, kelaInvoiced=False)
            for ss in ccsessions:
                sic = KelaInvoiceLineItem(
                    date = ss.date,
                    time = ss.time,
                    sessionInvoiceType = ss.sessionInvoiceType,
                    kelaInvoiceType = ss.kelaInvoiceType,
                    sessionType = ss.sessionType,
                    sessionDone = ss.sessionDone,
                    kelaInvoiced = ss.kelaInvoiced,
                    customerInvoiced = ss.customerInvoiced,
                    kelaInvoice = invoice,
                    session = ss,
                    sessionprice = ss.sessionprice,
                    sessionpriceKelaRefund = ss.sessionpriceKelaRefund
                )
                sic.save()
        for i in invoicablesessions:
            i.kelaInvoiced = True
            i.save()
        # update monthlyrevenue table at api module
        update_api_monthlyrevenue.delay()

    def get_kelastatementcustomerlines(*args, **kwargs):
        """
            Find all customers that have invoicable sessions
        :param args:
        :param kwargs:
            'pk' of Kelastatement
        :return:

        """
        ks = get_object_or_404(KelaStatement, id=kwargs['pk'])
        ic = KelaInvoice.objects.filter(kelaStatement=ks).values('id')
        dd = []
        iline = []
        k = 1
        totalcount = 0
        for i in ic:
            icobj = get_object_or_404(KelaInvoice, id=i['id'])
            if icobj:
                sobj = KelaInvoiceLineItem.objects.filter(kelaInvoice=icobj).order_by('date')
                sagg = sobj.aggregate(kelaRefundTotal = Sum('sessionpriceKelaRefund'), max_date = Max('date'), min_date = Min('date'))
                iline.append({
                    'id': icobj.id,
                    'firstName': icobj.kelaInvoiceCustomer.firstName,
                    'lastName': icobj.kelaInvoiceCustomer.lastName,
                    'additionalName': icobj.kelaInvoiceCustomer.additionalName,
                    'ssn': icobj.kelaInvoiceCustomer.ssn,
                    'kelaRefundTotal': sagg['kelaRefundTotal'],
                    'minSessionDate': sagg['min_date'],
                    'maxSessionDate': sagg['max_date'],
                    'linenum': k
                })
                totalcount += sagg['kelaRefundTotal']
                k += 1
        dd= {
            'totalRefund': totalcount,
            'count': k-1,
            'invoicablecustomers': iline
        }
        return dd


    def get_kelainvoicablesessions(*args, **kwargs):
        """
           Finds all sessions that has been completed (sessionDone=True) and are not invoiced from Kela (kelaInvoiced=False)

        :param args:
        :param kwargs:
        :return:
        """
        #Find customers that has session that are not invoiced from Kela
        ic = Session.objects.filter(sessionDone=True, kelaInvoiced=False).values('customer').distinct()
        dd = []
        k=1
        for i in ic:

            icobj = get_object_or_404(Customer, id=i['customer'])
            if icobj:
                # Find Sessions of this Customer sorted by 'date'
                slist = Session.objects.filter(sessionDone=True, kelaInvoiced=False, customer=icobj).order_by('date')
                sagg = slist.aggregate(kelaRefundTotal = Sum('sessionpriceKelaRefund'), max_date = Max('date'), min_date = Min('date'))
                dd.append({
                    'id': icobj.id,
                    'firstName': icobj.firstName,
                    'lastName': icobj.lastName,
                    'additionalName': icobj.additionalName,
                    'invoicablesessions': slist,
                    'kelaRefundTotal': sagg['kelaRefundTotal'],
                    'minSessionDate': sagg['min_date'],
                    'maxSessionDate': sagg['max_date'],
                    'linenum': k

                }
                )
                k += 1
        return dd



    def __str__(self):
        return self.companyName

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('kelainvoicing:kelastatement_detail', args=[str(self.id)])


class KelaInvoiceCustomer(CustomerModel):
    """
        Used to store copy of Customer.
        Due to data in Invoice must not be changed after invoice has been sent
        Link to original Customer will be created
    """
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.lastName + ", " + self.firstName


class KelaInvoiceCompanyProfile(CompanyProfileModel):
    """
        Used to store copy of CompanyProfile.
        Due to data in Invoice must not be changed after invoice has been sent
        Link to original Customer will be created
    """

    companyProfile = models.ForeignKey(CompanyProfile)
    kelaStatement =  models.ForeignKey(KelaStatement)

    def __str__(self):
        return self.companyName


class KelaInvoice(CompanyProfileModel):
    """

    """
    kelaStatement = models.ForeignKey(KelaStatement)
    kelaInvoiceCustomer = models.ForeignKey(KelaInvoiceCustomer)
    date = models.DateField(null=True)
    paidDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('kelainvoicing:kelainvoice_detail', args=[str(self.id)])


    def get_kelainvoicelineitems(*args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        ki = get_object_or_404(KelaInvoice, id=kwargs['pk'])
        kili = KelaInvoiceLineItem.objects.filter(kelaInvoice=ki).order_by('date')
        iline = []
        dd = []
        k=1
        sagg = kili.aggregate(kelaRefundTotal = Sum('sessionpriceKelaRefund'), max_date = Max('date'), min_date = Min('date'))
        for icobj in kili:
            #icobj = get_object_or_404(KelaInvoiceLineItem, id=i['id'])

            #TODO: Calculate total Kelacost for Customer 'kelaTotalCustomerCost'
            #TODO: Create Duration text between first and last currenly invoicable session 'sessionDuration'
            iline.append({
                'date': icobj.date,
            'sessionType': icobj.sessionType,
             'sessionprice': icobj.sessionprice,
            'sessionpriceKelaRefund': icobj.sessionpriceKelaRefund,
                'linenum': k

            }
            )
            k += 1
        dd = {
            'sessions': iline,
            'sessioncount': k - 1,
            'kelaRefundTotal': sagg['kelaRefundTotal']
        }
        return dd


class KelaInvoiceLineItem(SessionModel):
    """
        Used to store copy of Session
        Due to data in Invoice must not be changed after invoice has been sent
        Link to original Session will be created
    """
    kelaInvoice = models.ForeignKey(KelaInvoice)
    session = models.ForeignKey(Session)

    def __str__(self):
        return str(self.date) + " " + str(self.time)

    # allow views to automatically send user to the detail view of the object after creating or updating object


#
