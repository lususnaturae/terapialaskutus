# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import template
from django.db import models
from django.core.urlresolvers import reverse

register = template.Library()


class TimeStampedModel(models.Model):
    """
        An Abstract base class that provides
        self updating ''created'' and ''modified'' fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class CustomerModel(TimeStampedModel):
    """
        Customer base model
    """
    THERAPY_CATEGORY_CHOICES = {
        ('KUNTOUTUS', 'Kuntoutusterapia'),
        ('NEUROPSYKOLOGINEN', 'Neuropsykologinen kuntoutus'),
        ('MUSIIKKI', 'Musiikkiterapia'),
        ('LAUSUNTO', 'Lausunto'),
        ('MUUSYY', 'Muuta, mikä?')
    }

    firstName = models.CharField(max_length=120)
    additionalName = models.CharField(max_length=120, blank=True)
    lastName = models.CharField(max_length=120)
    ssn =  models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    zipCode = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    status = models.BooleanField(default=True)
    therapyCategory = models.CharField(max_length=40, default='KUNTOUTUS', choices=THERAPY_CATEGORY_CHOICES)
    sessionprice = models.DecimalField(max_digits=5, decimal_places=2)
    sessionpriceKelaRefund = models.DecimalField(max_digits=5, decimal_places=2)
    # statementpriceKela = models.DecimalField(max_digits=5, decimal_places=2)

    def sessionCostToCustomer(self):
        return self.sessionprice - self.sessionpriceKelaRefund

    class Meta:
        abstract=True


class Customer(CustomerModel):
    """
        Customer basic information.
        Inherits from abstract model CustomerModel
    """
    def __str__(self):
        return self.lastName + ", " + self.firstName

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('customers:customer_detail', args=[str(self.id)])


class SessionModel(TimeStampedModel):
    """
    Therapy session abstract model
    """
    SESSION_INVOICE_CHOICES = {
        ('FREEINTRODUCTION','Ilmainen tutustumiskäynti'),
        ('HALFPRICEINTRODUCTION','Tutustumiskäynti puoleenhintaan'),
        ('SINGLESESSION', 'Terapiakäynti'),
        ('DOUBLESESSION', 'Kaksoiskäynti')
    }
    KELAINVOICABLE_CHOICES = {
        ('CANINVOICEKELA', 'Kela maksaa osan käynnistä'),
        ('NOKELAINVOICE', 'Kela ei maksa käyntiä')
    }
    SESSION_TYPE_CHOICES = {
        ('YKSILÖ', 'Yksilöterapia'),
        ('LAUSUNTO', 'Lausunto'),
        ('RYHMÄ', 'Ryhmäkäynti'),
        ('PERHE', 'Perhekäynti'),
        ('PARI', 'Parikäynti'),
        ('OHJAUS', 'Ohjauskäynti'),
        ('MUU', 'Muu käynti')
    }

    date = models.DateField()
    time = models.TimeField()
    sessionInvoiceType = models.CharField(max_length=40, default='SINGLESESSION', choices=SESSION_INVOICE_CHOICES)
    kelaInvoiceType = models.CharField(max_length=40, default='CANINVOICEKELA', choices=KELAINVOICABLE_CHOICES)
    sessionType = models.CharField(max_length=40, default='YKSILÖ', choices=SESSION_TYPE_CHOICES)
    sessionDone = models.BooleanField(default=False)
    kelaInvoiced = models.BooleanField(default=False)
    customerInvoiced = models.BooleanField(default=False)
    sessionprice = models.DecimalField(max_digits=5, decimal_places=2)
    sessionpriceKelaRefund = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract=True


class Session(SessionModel):
    """
    Therapy session.
    """
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return str(self.date)

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
        return reverse('customers:session_detail', args=[str(self.id)])


class CompanyProfileModel(TimeStampedModel):
    """
    CompanyProfile base abstract class
    """
    SERVICEPROVIDER_TYPE_CHOICES = {
        ('PALVELUNTUOTTAJA','Kuntoutuspalvelutuottaja'),
        ('LASKUTTAJA','Laskuttaja kuntoutuspalveluntuottajan puolesta')
    }
    INVOICEREF_TYPE_CHOICES = {
        ('TILITYSNRO','Tilityksen numero'),
        ('VIITENUMERO', 'Viitenumero')
    }
    TAX_ADVANCE_COLLECTION_TYPE_CHOICES = {
        ('TAXREGISTER', "Ennakkoperintärekisterissä"),
        ('TAXDEDUCTIONCARD','Verokortti')
    }

    companyName = models.CharField(max_length=120)
    firstName = models.CharField(max_length=120)
    additionalName = models.CharField(max_length=120, blank=True)
    lastName = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    zipCode = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True)
    telephone = models.CharField(max_length=120, blank=True)
    email = models.EmailField( blank=True)
    vatId = models.CharField(max_length=20)
    iban = models.CharField(max_length=40)
    bic = models.CharField(max_length=40)
    serviceproviderType = models.CharField(max_length=40, default='PALVELUNTUOTTAJA', choices=SERVICEPROVIDER_TYPE_CHOICES)
    invoiceRefType = models.CharField(max_length=40, default='TILITYSNRO', choices=INVOICEREF_TYPE_CHOICES)
    taxAdvanceType = models.CharField(max_length=40, default='TAXREGISTER', choices=TAX_ADVANCE_COLLECTION_TYPE_CHOICES)

    class Meta:
        abstract=True


class CompanyProfile(CompanyProfileModel):
    """
    Basic information about own company that is needed when invoices are created.
    Only one CompanyProfile can be created
    """
    def __str__(self):
        return self.companyName

    # allow views to automatically send user to the detail view of the object after creating or updating object
    def get_absolute_url(self):
       return reverse('customers:companyprofile_detail', args=[str(self.id)])


    def get_or_create_companyprofile():
        """
        Gets companyprofile or creates new if it does not exist
        :return: CompanyProfile object
        """

        if CompanyProfile.objects.all().exists():
            cp = CompanyProfile.objects.all()[:1].get()
        else:
            cp = CompanyProfile(
                id = 9999,
                companyName = 'Esimerkki Terapia Oy',
                firstName = 'Etunimi',
                additionalName = '',
                lastName = 'Sukunimi',
                address = 'Terapeuttipolku 1',
                zipCode = '33100',
                city = 'TAMPERE',
                country = 'Finland',
                telephone = '0451234567',
                email = 'etunimi.sukunimi@eioikea.fi',
                vatId = '1234567-1',
                iban = 'FI3131301232432432',
                bic = 'HANDIFF',
                serviceproviderType = 'PALVELUNTUOTTAJA',
                invoiceRefType = 'TILITYSNRO',
                taxAdvanceType = 'TAXREGISTER',
            )
            cp.save()
        return cp
