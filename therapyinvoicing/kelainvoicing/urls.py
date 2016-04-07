from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^kelacontact/(?P<pk>[0-9]+)/update/$',
        views.KelaContactProfileUpdateView.as_view(),
        name='kelacontactprofile_update'),
    url(r'^kelastatement/$',
         views.KelaStatementListView.as_view(),
         name='kelastatement_list'),
    url(r'^kelastatement/(?P<pk>[0-9]+)/$',
        views.KelaStatementDetailView.as_view(),
        name='kelastatement_detail'),
    url(r'^kelastatement/create/$',
        views.KelaStatementCreateView.as_view(),
        name='kelastatement_create'),
    url(r'^kelastatement/(?P<pk>[0-9]+)/update/$',
        views.KelaStatementUpdateView.as_view(),
        name='kelastatement_update'),
    url(r'^kelastatement/(?P<pk>[0-9]+)/delete/$',
        views.KelaStatementDeleteView.as_view(),
        name='kelastatement_delete'),
    url(r'^kelainvoice/(?P<pk>[0-9]+)/$',
        views.KelaInvoiceDetailView.as_view(),
        name='kelainvoice_detail'),
]
