import factory
import datetime
from django.utils import timezone
from ...customers.tests.factories import CustomerFactory, CompanyProfileFactory, SessionFactory, SessionDoneFactory


class KelaContactProfileFactory(factory.django.DjangoModelFactory):

    legalName="TestLegalName"
    firstName="TestFirstNameWithåäöÅÄÖ"
    additionalName="TestAdditionalName"
    lastName="TestLastName"
    address="TestAddress"
    zipCode="TestZipCode"
    city="TestCity"
    country="TestCountry"

    class Meta:
        model = 'kelainvoicing.KelaContactProfile'
        django_get_or_create = ('legalName', 'address', 'zipCode', 'city' )


class KelaStatementFactory(factory.django.DjangoModelFactory):

    companyName = 'Esimerkki Terapia Oy'
    firstName = 'Etunimi'
    additionalName = 'Muut nimet'
    lastName = 'Sukunimi'
    address = 'Terapeuttipolku 1'
    zipCode = '33100'
    city = 'TAMPERE'
    country = 'Finland'
    telephone = '0451234567'
    email = 'etunimi.sukunimi@eioleoikea.fi'
    vatId = '1234567-1'
    iban = 'FI3131301232432432'
    bic = 'HANDIFF'
    serviceproviderType = 'PALVELUNTUOTTAJA'
    invoiceRefType = 'TILITYSNRO'
    taxAdvanceType = 'TAXREGISTER'
    date = timezone.now().date()
    orderno = "001"
    invoiceRef = "12345678"
    taxAdvanceExplanation = "testexplanation"

    class Meta:
        model = 'kelainvoicing.KelaStatement'
        django_get_or_create = ('companyName', )


class KelaInvoiceCustomerFactory(factory.django.DjangoModelFactory):

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
        model = 'kelainvoicing.KelaInvoiceCustomer'
        django_get_or_create = ('lastName', 'firstName' )


class KelaInvoiceCompanyProfileFactory(factory.django.DjangoModelFactory):

    companyProfile = factory.SubFactory(CompanyProfileFactory)
    kelaStatement = factory.SubFactory(KelaStatementFactory)
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
        model = 'kelainvoicing.KelaInvoiceCompanyProfile'
        django_get_or_create = ('companyName', 'vatId', )


class KelaInvoiceFactory(factory.django.DjangoModelFactory):

    kelaStatement = factory.SubFactory(KelaStatementFactory)
    kelaInvoiceCustomer = factory.SubFactory(KelaInvoiceCustomerFactory)
    date = timezone.now().date()
    paidDate = timezone.now().date()

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
        model = 'kelainvoicing.KelaInvoice'
        django_get_or_create = ('companyName', 'vatId', )


class KelaInvoiceLineItemFactory(factory.django.DjangoModelFactory):

    kelaInvoice = factory.SubFactory(KelaInvoiceFactory)
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
        model = 'kelainvoicing.KelaInvoiceLineItem'
        django_get_or_create = ('date', 'time', )
