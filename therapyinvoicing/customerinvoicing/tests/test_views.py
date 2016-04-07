from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse

from test_plus.test import TestCase
from .factories import InvoiceFactory
from ...customers.tests.factories import CompanyProfileFactory

from ..views import (
    InvoiceDetailView,
    InvoiceListView,
    InvoiceGenerateConfirmTemplateView,
    InvoiceCreatorRedirectView,

)


class InvoiceViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User = get_user_model()

        self.user = User.objects.create_user(
            username='testuser', email='testuser@eioleoikea.fi', password='top_secret'
        )
        g = Group.objects.get_or_create(name=u'therapist')
        self.user.groups.add(g[0].pk)

    def test_detailview_get(self):
        obj = InvoiceFactory.create_batch(1).pop()
        request = self.factory.get(reverse("customerinvoicing:invoice_detail",  kwargs={'pk': obj.pk}))
        request.user = self.user
        response = InvoiceDetailView.as_view()(request, pk=obj.pk)
        self.assertEqual(response.status_code, 200)

    def test_listview_get(self):
        request = self.factory.get(reverse("customerinvoicing:invoice_list"))
        request.user = self.user

        response = InvoiceListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_invoicegenerateconfirmtemplateview_get(self):
        request = self.factory.get(reverse("customerinvoicing:invoice_generator_confirm"))
        request.user = self.user

        response = InvoiceGenerateConfirmTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_invoicecreatorredirectview_get(self):
        CompanyProfileFactory.create_batch(1)
        request = self.factory.get(reverse("customerinvoicing:invoice_creator_all"))
        request.user = self.user

        response = InvoiceCreatorRedirectView.as_view()(request)
        self.assertEqual(response.status_code, 302)




