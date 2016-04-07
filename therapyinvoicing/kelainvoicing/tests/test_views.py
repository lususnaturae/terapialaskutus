from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse

from test_plus.test import TestCase
from .factories import KelaContactProfileFactory, KelaStatementFactory
from .factories import KelaInvoiceFactory
from ...customers.tests.factories import CompanyProfileFactory

from ..views import (
    KelaContactProfileUpdateView,
    KelaInvoiceDetailView,
    KelaStatementCreateView,
    KelaStatementDeleteView,
    KelaStatementDetailView,
    KelaStatementListView,
    KelaStatementUpdateView,
)


class KelaContactProfileViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_updateview_get(self):
        obj = KelaContactProfileFactory.create_batch(1).pop()
        request = self.factory.get(reverse("kelainvoicing:kelacontactprofile_update",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = KelaContactProfileUpdateView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)


class KelaInvoiceViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_detailview_get(self):
        obj = KelaInvoiceFactory.create_batch(1).pop()
        request = self.factory.get(reverse("kelainvoicing:kelainvoice_detail",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = KelaInvoiceDetailView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)


class KelaStatementViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_createview_get(self):
        CompanyProfileFactory.create_batch(1)
        request = self.factory.get(reverse("kelainvoicing:kelastatement_create"))
        request.user = self.user

        response = KelaStatementCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_updateview_get(self):
        obj = KelaStatementFactory.create_batch(1).pop()
        request = self.factory.get(reverse("kelainvoicing:kelastatement_update",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = KelaStatementUpdateView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)

    def test_deleteview_get(self):
        obj = KelaStatementFactory.create_batch(1).pop()
        request = self.factory.get(reverse("kelainvoicing:kelastatement_delete",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = KelaStatementDeleteView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)

    def test_detailview_get(self):
        obj = KelaStatementFactory.create_batch(1).pop()
        request = self.factory.get(reverse("kelainvoicing:kelastatement_detail",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = KelaStatementDetailView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)

    def test_listview_get(self):
        request = self.factory.get(reverse("kelainvoicing:kelastatement_list"))
        request.user = self.user

        response = KelaStatementListView.as_view()(request)
        self.assertEqual(response.status_code, 200)



