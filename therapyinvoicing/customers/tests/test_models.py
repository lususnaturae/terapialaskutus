from django.utils import timezone
import time
from datetime import timedelta
import unittest
from test_plus.test import TestCase
from ..models import Customer
from ..models import Session
from ..models import CompanyProfile


class CustomerTest(TestCase):

    def create_customer(self, firstname="TestFirstNameWithåäöÅÄÖ", additionalname="TestAdditionalName",
                        lastname="TestLastName",ssn="TestSsn", address="TestAddress",
                        zipcode="TestZipCode", city="TestCity", country="TestCountry",
                        telephone="TestTelephone", email="TestEmail@testdomain.com", status=True, therapyCategory="KUNTOUTUS",
                        sessionprice=85.00, sessionpriceKelaRefund=52.14,statementpriceKela=22.17):
        return Customer.objects.create(firstName=firstname, additionalName=additionalname, lastName=lastname,
                        ssn=ssn, address=address, zipCode=zipcode, city=city, country=country,
                        telephone=telephone, email=email, status=status, therapyCategory=therapyCategory, sessionprice=sessionprice,
                        sessionpriceKelaRefund=sessionpriceKelaRefund,statementpriceKela=statementpriceKela)

    def test_customer_creation(self):
        w = self.create_customer()
        self.assertTrue(isinstance(w, Customer))
        self.assertEqual(w.__str__(), w.lastName + ", " + w.firstName)
        self.assertAlmostEqual(w.created, w.modified, delta=timedelta(seconds=1))

    def test_customer_updatedwhensaving(self):
        w = self.create_customer()
        time.sleep(0.0001)
        w.save()
        self.assertNotEqual(w.created, w.modified)

    def test_get_absolute_url(self):
        c = self.create_customer()
        self.assertEqual(
            c.get_absolute_url(),
            '/customers/customer/' + str(c.id) + '/'
        )


class SessionTest(TestCase):

    def create_customer(self, firstname="TestFirstNameWithåäöÅÄÖ", additionalname="TestAdditionalName",
                        lastname="TestLastName",ssn="TestSsn", address="TestAddress",
                        zipcode="TestZipCode", city="TestCity", country="TestCountry",
                        telephone="TestTelephone", email="TestEmail@testdomain.com", status=True, therapyCategory="KUNTOUTUS",
                        sessionprice=85.00, sessionpriceKelaRefund=52.14,statementpriceKela=22.17):
        return Customer.objects.create(firstName=firstname, additionalName=additionalname, lastName=lastname,
                        ssn=ssn, address=address, zipCode=zipcode, city=city, country=country,
                        telephone=telephone, email=email, status=status, therapyCategory=therapyCategory, sessionprice=sessionprice,
                        sessionpriceKelaRefund=sessionpriceKelaRefund,statementpriceKela=statementpriceKela)

    def create_session(self, customer, date=timezone.now().date(), time=timezone.now().time(), sessionInvoiceType="SINGLESESSION",
                       kelaInvoiceType="CANINVOICEKELA", sessionType="YKSILÖ",
                        sessionprice=85.00, sessionpriceKelaRefund=52.14, sessionDone=False, kelaInvoiced=False):
        return Session.objects.create(customer=customer, date=date, time=time, sessionInvoiceType=sessionInvoiceType,
                                      kelaInvoiceType=kelaInvoiceType, sessionType=sessionType, sessionprice=sessionprice,
                                      sessionpriceKelaRefund=sessionpriceKelaRefund,
                                      sessionDone=sessionDone, kelaInvoiced=kelaInvoiced)

    def test_session_creation(self):
        w = self.create_customer()
        self.assertTrue(isinstance(w, Customer))
        self.assertEqual(w.__str__(), w.lastName + ", " + w.firstName)
        x = self.create_session(w)
        self.assertTrue(isinstance(x, Session))
        self.assertAlmostEqual(w.created, w.modified, delta=timedelta(seconds=1))

    def test_session_updatedwhensaving(self):
        c = self.create_customer()
        s = self.create_session(c)
        self.assertTrue(isinstance(s, Session))
        time.sleep(0.0001)
        s.save()
        self.assertNotEqual(s.created, s.modified)

    def test__str__(self):
        c = self.create_customer()
        s = self.create_session(c)
        self.assertEqual(
            s.__str__(),
            str(timezone.now().date())
        )

    def test_get_absolute_url(self):
        c = self.create_customer()
        s = self.create_session(c)
        self.assertEqual(
            s.get_absolute_url(),
            '/customers/session/' + str(s.id) + '/'
        )


class CompanyProfileTest(TestCase):

    def create_companyprofile(self, companyname="TestCompanyName", firstname="TestFirstNameWithåäöÅÄÖ", additionalname="TestAdditionalName",
                        lastname="TestLastName", address="TestAddress",
                        zipcode="TestZipCode", city="TestCity", country="TestCountry",
                        telephone="TestTelephone", email="TestEmail@testdomain.com",vatid="TestVatId", iban="TestBankAccount", bic="TestBank",
                              serviceproviderType="PALVELUNTUOTTAJA"):
        return CompanyProfile.objects.create(id=9999, companyName=companyname, firstName=firstname, additionalName=additionalname, lastName=lastname,
                         address=address, zipCode=zipcode, city=city, country=country,
                        telephone=telephone, email=email, vatId=vatid, iban=iban, bic=bic, serviceproviderType=serviceproviderType)

    def test_companyprofile_creation(self):
        w = self.create_companyprofile()
        self.assertTrue(isinstance(w, CompanyProfile))
        self.assertEqual(w.__str__(), w.companyName)
        self.assertAlmostEqual(w.created, w.modified, delta=timedelta(seconds=1))

    def test_companyprofile_updatedwhensaving(self):
        cp = self.create_companyprofile()
        time.sleep(0.0001)
        cp.save()
        self.assertNotEqual(cp.created, cp.modified)

    def test_get_or_create_companyprofile(self):
        self.assertFalse(CompanyProfile.objects.all().exists()), "CompanyProfile should not exist"
        cp = CompanyProfile.get_or_create_companyprofile()
        self.assertTrue(CompanyProfile.objects.all().exists()), "CompanyProfile was not created"
        self.assertEqual(CompanyProfile.objects.all().count(), 1), "Only one CompanyProfile should exist"
        cp = CompanyProfile.get_or_create_companyprofile()
        self.assertEqual(CompanyProfile.objects.all().count(), 1), "additional CompanyProfile was created"

    def test_get_absolute_url(self):
        cp = self.create_companyprofile()
        self.assertEqual(cp.get_absolute_url(),'/customers/companyprofile/9999/'), "companyprofile get_absolute_url wrong"


if __name__ == '__main__':
    unittest.main()

