from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse, reverse_lazy
from test_plus.test import TestCase
from .factories import CustomerFactory, SessionFactory, CompanyProfileFactory
from ..models import CompanyProfile, Customer

from ..views import (
    CustomerCreateView,
    CustomerListView,
    SessionCreateView,
    SessionDetailView,
    SessionListView,
    SessionUpdateView,
    SessionDeleteView,
    CompanyProfileUpdateView,
    CompanyProfileDetailView,
)


class CustomerViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_customer_list_get(self):

        request = self.factory.get(reverse("customers:customer_list"))
        request.user = self.user

        response = CustomerListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_customer_create_get(self):

        request = self.factory.get(reverse("customers:customer_create"))
        request.user = self.user

        response = CustomerCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_customer_detail_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()

        request = self.factory.get(reverse("customers:customer_detail",  kwargs={'pk': testcustomer.pk}))
        request.user = self.user

        response = CustomerCreateView.as_view()(request, pk=testcustomer.pk)
        self.assertEqual(response.status_code, 200)

    def test_customer_update_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        request = self.factory.get(reverse("customers:customer_update",  kwargs={'pk': testcustomer.pk}))
        request.user = self.user

        response = CustomerCreateView.as_view()(request, pk=testcustomer.pk)
        self.assertEqual(response.status_code, 200)

    def test_customer_delete_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        request = self.factory.get(reverse("customers:customer_delete",  kwargs={'pk': testcustomer.pk}))
        request.user = self.user

        response = CustomerCreateView.as_view()(request, pk=testcustomer.pk)
        self.assertEqual(response.status_code, 200)


class SessionViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_session_list_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        cu = Customer.objects.all()[:1].get()

        request = self.factory.get(reverse_lazy("customers:session_list", kwargs={'pk': cu.pk}))
        request.user = self.user

        response = SessionListView.as_view()(request, pk=cu.pk)
        self.assertEqual(response.status_code, 200)

    def test_session_create_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        request = self.factory.get(reverse_lazy("customers:session_create", kwargs={'pk': testcustomer.pk}))
        request.user = self.user

        response = SessionCreateView.as_view()(request, pk=testcustomer.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['savebuttontext'], "Tallenna")

    def test_session_detail_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(1, customer=testcustomer))
        testsession = testsessions.pop()
        request = self.factory.get(reverse_lazy("customers:session_detail",  kwargs={'pk': testsession.pk}))
        request.user = self.user

        response = SessionDetailView.as_view()(request, pk=testsession.pk)
        self.assertEqual(response.status_code, 200)

    def test_session_update_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(1, customer=testcustomer))
        testsession = testsessions.pop()
        request = self.factory.get(reverse_lazy("customers:session_update",  kwargs={'pk': testsession.pk}))
        request.user = self.user

        response = SessionUpdateView.as_view()(request, pk=testsession.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['savebuttontext'], "Tallenna")

    def test_session_delete_get(self):

        testcustomers = []
        testcustomers.extend(CustomerFactory.create_batch(1))
        testcustomer = testcustomers.pop()
        testsessions = []
        testsessions.extend(SessionFactory.create_batch(1, customer=testcustomer))
        testsession = testsessions.pop()
        request = self.factory.get(reverse_lazy("customers:session_delete",  kwargs={'pk': testsession.pk}))
        request.user = self.user

        response = SessionDeleteView.as_view()(request, pk=testsession.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['deleteconfirmationbuttontext'], "Vahvista tapaamisen poistaminen")


class CompanyProfileViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)
        testcompanyprofiles = []
        testcompanyprofiles.extend(CompanyProfileFactory.create_batch(1))

    def test_companyprofile_detail_get(self):

        companyprofilecount = CompanyProfile.objects.count()
        if companyprofilecount == 0:
            testcompanyprofiles = []
            testcompanyprofiles.extend(CompanyProfileFactory.create_batch(1))
            testcompanyprofile = testcompanyprofiles.pop()
        else:
            testcompanyprofile  = CompanyProfile.objects.all()[:1].get()

        request = self.factory.get(reverse("customers:companyprofile_detail",  kwargs={'pk': testcompanyprofile.pk}))
        request.user = self.user

        response = CompanyProfileDetailView.as_view()(request, pk=testcompanyprofile.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['companyprofile'], testcompanyprofile)

    def test_companyprofile_update_get(self):

        testcompanyprofile  = CompanyProfile.objects.all()[:1].get()

        request = self.factory.get(reverse("customers:companyprofile_update",  kwargs={'pk': testcompanyprofile.pk}))
        request.user = self.user

        response = CompanyProfileUpdateView.as_view()(request, pk=testcompanyprofile.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['companyprofile'], testcompanyprofile)
