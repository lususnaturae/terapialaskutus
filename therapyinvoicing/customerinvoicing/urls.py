from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^invoicecreator/$',
        views.InvoiceCreatorRedirectView.as_view(),
        name='invoice_creator_all'),
    url(r'^customerinvoice/$',
        views.InvoiceListView.as_view(),
        name='invoice_list'),
    url(r'^customerinvoice/(?P<pk>[0-9]+)/$',
        views.InvoiceDetailView.as_view(),
        name='invoice_detail'),
    url(r'^customerinvoice/generateinvoice/$',
        views.InvoiceGenerateConfirmTemplateView.as_view(),
        name='invoice_generator_confirm'),
]


