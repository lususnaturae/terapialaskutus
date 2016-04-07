import factory
import datetime
from django.utils import timezone
from ...customers.tests.factories import CustomerFactory, CompanyProfileFactory, SessionFactory


class InvoiceCustomerFactory(factory.django.DjangoModelFactory):

    customer = factory.SubFactory(CustomerFactory)
    firstName = factory.Sequence(lambda n: 'firstname-{0}'.format(n))
    lastName = factory.Sequence(lambda n: 'lastname-{0}'.format(n))
    additionalName = factory.Sequence(lambda n: 'additionalName-{0}'.format(n))
    ssn = factory.Sequence(lambda n: 'ssn-{0}'.format(n))
    address = factory.Sequence(lambda n: 'address-{0}'.format(n))
    zipCode = factory.Sequence(lambda n: 'zipCode-{0}'.format(n))
    city = factory.Sequence(lambda n: 'city-{0}'.format(n))
    country = factory.Sequence(lambda n: 'country-{0}'.format(n))
    telephone = factory.Sequence(lambda n: 'telephone-{0}'.format(n))
    email = factory.Sequence(lambda n: 'email-{0}@example.com'.format(n))
    status = True
    therapyCategory = 'KUNTOUTUS'
    sessionprice = 80
    sessionpriceKelaRefund = 52.14
    statementpriceKela = 22.17

    class Meta:
        model = 'customerinvoicing.InvoiceCustomer'
        django_get_or_create = ('lastName', 'firstName' )


class InvoiceCompanyProfileFactory(factory.django.DjangoModelFactory):

    companyProfile = factory.SubFactory(CompanyProfileFactory)
    companyName = 'Esimerkki Terapia Oy'
    firstName = 'Etunimi'
    additionalName = ''
    lastName = 'Sukunimi'
    address = 'Terapeuttipolku 1'
    zipCode = '33100'
    city = 'TAMPERE'
    country = ''
    telephone = ''
    email = ''
    vatId = '1234567-1'
    iban = 'FI3131301232432432'
    bic = 'HANDIFF'
    serviceproviderType = 'PALVELUNTUOTTAJA'
    invoiceRefType = 'TILITYSNRO'
    taxAdvanceType = 'TAXREGISTER'

    class Meta:
        model = 'customerinvoicing.InvoiceCompanyProfile'
        django_get_or_create = ('companyName', 'vatId', )


class InvoiceFactory(factory.django.DjangoModelFactory):

    invoiceCustomer = factory.SubFactory(InvoiceCustomerFactory)
    invoiceCompanyProfile = factory.SubFactory(InvoiceCompanyProfileFactory)
    date = timezone.now().date()
    invoiceNumber = factory.Sequence(lambda n: '{0}'.format(n))
    paidDate = timezone.now().date()


    class Meta:
        model = 'customerinvoicing.Invoice'
        django_get_or_create = ('invoiceNumber', )


class InvoiceLineItemFactory(factory.django.DjangoModelFactory):

    invoice = factory.SubFactory(InvoiceFactory)
    session = factory.SubFactory(SessionFactory)
    date = factory.Sequence(lambda n: datetime.date(2016, 1, 15) + datetime.timedelta(days=(n * 7)))
    time = datetime.time(12,30,00)
    sessionInvoiceType = 'SINGLESESSION'
    kelaInvoiceType = 'CANINVOICEKELA'
    sessionType = 'YKSILÖ'
    sessionDone =False
    kelaInvoiced = False
    customerInvoiced = False
    sessionprice = 80
    sessionpriceKelaRefund = 52.14

    class Meta:
        model = 'customerinvoicing.InvoiceLineItem'
        django_get_or_create = ('date', 'time', )
