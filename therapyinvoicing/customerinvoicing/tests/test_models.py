import time
import unittest
from test_plus.test import TestCase
from datetime import timedelta
from ..models import InvoiceCompanyProfile, Invoice, InvoiceLineItem, InvoiceCustomer
from ...customers.tests.factories import SessionDoneFactory, CompanyProfileFactory
from .factories import InvoiceFactory, InvoiceCompanyProfileFactory, InvoiceLineItemFactory, InvoiceCustomerFactory


class InvoiceCustomerTest(TestCase):

    def test_creation(self):
        obj = InvoiceCustomerFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, InvoiceCustomer)), "Invoice object creation not working"
        self.assertEqual(obj.__str__(), obj.lastName + ', ' + obj.firstName), "Invoice __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = InvoiceCustomerFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class InvoiceCompanyProfileTest(TestCase):

    def test_creation(self):
        obj = InvoiceCompanyProfileFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, InvoiceCompanyProfile)), "InvoiceCompanyProfile object creation not working"
        self.assertEqual(obj.__str__(), obj.companyName), "InvoiceCompanyProfile __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = InvoiceCompanyProfileFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


class InvoiceTest(TestCase):

    def test_creation(self):
        obj = InvoiceFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, Invoice)), "Invoice object creation not working"
        self.assertEqual(obj.__str__(), str(obj.date)), "Invoice __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_get_absolute_url(self):
        cp = InvoiceFactory.create_batch(1).pop()
        self.assertEqual(cp.get_absolute_url(),'/customerinvoicing/customerinvoice/' + str(cp.pk) + '/'), "get_absolute_url wrong"

    def test_updatedwhensaving(self):
        obj = InvoiceFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)

    def test_create_invoices(self):
        #creates session with sessionDone=True
        CompanyProfileFactory.create_batch(1)
        # create 10 sessions for 10 customers
        SessionDoneFactory.create_batch(10)
        Invoice.create_invoices()
        self.assertEqual(Invoice.objects.all().count(), 10)

    def test_get_customerinvoicablesessions(self):
        # creates session with sessionDone=True
        SessionDoneFactory.create_batch(4)
        self.assertEqual(Invoice.get_customerinvoicablesessions().__len__(), 4)

    def test_get_invoicelineitems(self):
        obj = InvoiceLineItemFactory.create_batch(1).pop()
        self.assertEqual(InvoiceLineItem.get_invoicelineitems(pk=obj.invoice.pk)['invoiceTotalWithoutKelaRefund'], 80)


class InvoiceLineItemTest(TestCase):

    def test_creation(self):
        obj = InvoiceLineItemFactory.create_batch(1).pop()
        self.assertTrue(isinstance(obj, InvoiceLineItem)), "InvoiceLineItem object creation not working"
        self.assertEqual(obj.__str__(), str(obj.date) + " " + str(obj.time)), "InvoiceLineItem __str__ not returning correct string"
        self.assertAlmostEqual(obj.created, obj.modified, delta=timedelta(seconds=1))

    def test_updatedwhensaving(self):
        obj = InvoiceLineItemFactory.create_batch(1).pop()
        time.sleep(0.0001)
        obj.save()
        self.assertNotEqual(obj.created, obj.modified)


if __name__ == '__main__':
    unittest.main()

