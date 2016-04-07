import unittest
import time
from datetime import timedelta
from test_plus.test import TestCase
from ..models import KelaContactProfile
from ..models import KelaStatement, KelaInvoiceCustomer, KelaInvoiceCompanyProfile
from ..models import KelaInvoice, KelaInvoiceLineItem
from ...customers.tests.factories import CompanyProfileFactory
from .factories import KelaContactProfileFactory, KelaStatementFactory
from .factories import KelaInvoiceCustomerFactory, SessionDoneFactory
from .factories import KelaInvoiceCompanyProfileFactory
from .factories import KelaInvoiceFactory
from .factories import KelaInvoiceLineItemFactory


class KelaContactProfileTest(TestCase):

    def test_creation(self):
        obj = KelaContactProfileFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaContactProfile))
        self.assertEqual(obj.__str__(), obj.legalName)
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_get_absolute_url(self):
        obj = KelaContactProfileFactory.create_batch(1).pop()
        self.assertEqual(
            obj.get_absolute_url(),
            '/kelainvoicing/kelacontact/' + str(obj.id) + '/update/'
        )

    def test_updatedwhensaving(self):
        obj = KelaContactProfileFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)

    def test_get_or_create_kelacontactprofile_with_existing_profile(self):
        KelaContactProfileFactory.create_batch(1)
        self.assertTrue(KelaContactProfile.objects.exists()), "KelaContactProfile is not empty"
        obj = KelaContactProfile.get_or_create_kelacontactprofile()
        self.assertTrue(KelaContactProfile.objects.exists()), "KelaContactProfile is empty"
        self.assertEqual(KelaContactProfile.objects.count(), 1), "More than 1 KelaContactProfile"

    def test_get_or_create_kelacontactprofile_with_nonexisting_profile(self):
        self.assertFalse(KelaContactProfile.objects.exists()), "KelaContactProfile is not empty"
        obj = KelaContactProfile.get_or_create_kelacontactprofile()
        self.assertTrue(KelaContactProfile.objects.exists()), "KelaContactProfile is empty"
        self.assertEqual(KelaContactProfile.objects.count(), 1), "More than 1 KelaContactProfile"


class KelaStatementTest(TestCase):

    def test_creation(self):
        obj = KelaStatementFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaStatement)), "Kelastatement object creation not working"
        self.assertEqual(obj.__str__(), obj.companyName), "Kelastatement __str__ not returing companyName"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_get_kelastatementcustomerlines(self):
        obj = KelaInvoiceLineItemFactory.create_batch(4).pop()
        self.assertEqual(KelaStatement.get_kelastatementcustomerlines(pk=obj.kelaInvoice.kelaStatement.pk)['count'], 1)

    def test_get_kelainvoicablesessions(self):
        #creates session with sessionDone=True
        SessionDoneFactory.create_batch(4)
        self.assertEqual(KelaStatement.get_kelainvoicablesessions().__len__(), 4)

    def test_create_kelainvoices(self):
        CompanyProfileFactory.create_batch(1)
        #creates 10 Sessions with sessionDone=True
        SessionDoneFactory.create_batch(10)
        obj = KelaStatementFactory.create_batch(1).pop()
        KelaStatement.create_kelainvoices(pk=obj.pk)
        self.assertEqual(KelaInvoice.objects.all().count(), 10)

    def test_updatedwhensaving(self):
        obj = KelaStatementFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class KelaInvoiceCustomerTest(TestCase):

    def test_creation(self):
        obj = KelaInvoiceCustomerFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaInvoiceCustomer)), "KelaInvoice object creation not working"
        self.assertEqual(obj.__str__(), obj.lastName + ', ' + obj.firstName), "KelaInvoice __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = KelaInvoiceCustomerFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class KelaInvoiceCompanyProfileTest(TestCase):

    def test_creation(self):
        obj = KelaInvoiceCompanyProfileFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaInvoiceCompanyProfile)), "KelaInvoiceCompanyProfile object creation not working"
        self.assertEqual(obj.__str__(), obj.companyName), "KelaInvoiceCompanyProfile __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = KelaInvoiceCompanyProfileFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class KelaInvoiceTest(TestCase):

    def test_creation(self):
        obj = KelaInvoiceFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaInvoice)), "KelaInvoice object creation not working"
        self.assertEqual(obj.__str__(), str(obj.date)), "KelaInvoice __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_get_kelainvoicelineitems(self):
        obj = KelaInvoiceLineItemFactory.create_batch(1).pop()
        self.assertEqual(KelaInvoice.get_kelainvoicelineitems(pk=obj.kelaInvoice.pk)['sessioncount'], 1)

    def test_get_absolute_url(self):
        cp = KelaInvoiceFactory.create_batch(1).pop()
        self.assertEqual(cp.get_absolute_url(),'/kelainvoicing/kelainvoice/' + str(cp.pk) + '/'), "companyprofile get_absolute_url wrong"

    def test_updatedwhensaving(self):
        obj = KelaInvoiceFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class KelaInvoiceLineItemTest(TestCase):

    def test_creation(self):
        obj = KelaInvoiceLineItemFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, KelaInvoiceLineItem)), "KelaInvoiceLineItem object creation not working"
        self.assertEqual(obj.__str__(), str(obj.date) + " " + str(obj.time)), "KelaInvoiceLineItem __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = KelaInvoiceLineItemFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)

if __name__ == '__main__':
    unittest.main()

