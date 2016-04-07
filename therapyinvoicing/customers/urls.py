from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',
        views.CustomerListView.as_view(),
        name='customer_list'),
    url(r'^customer/(?P<pk>[0-9]+)/$',
        views.CustomerDetailView.as_view(),
        name='customer_detail'),
    url(r'^customer/create/$',
        views.CustomerCreateView.as_view(),
        name='customer_create'),
    url(r'^customer/(?P<pk>[0-9]+)/update/$',
        views.CustomerUpdateView.as_view(),
        name='customer_update'),
    url(r'^customer/(?P<pk>[0-9]+)/delete/$',
        views.CustomerDeleteView.as_view(),
        name='customer_delete'),


    url(r'^companyprofile/(?P<pk>[0-9]+)/$',
        views.CompanyProfileDetailView.as_view(),
        name='companyprofile_detail'),

    url(r'^companyprofile/(?P<pk>[0-9]+)/update/$',
        views.CompanyProfileUpdateView.as_view(),
        name='companyprofile_update'),




    url(r'^customer/(?P<pk>[0-9]+)/session/list/$',
        views.SessionListView.as_view(),
        name='session_list'),
    url(r'^session/(?P<pk>[0-9]+)/$',
        views.SessionDetailView.as_view(),
        name='session_detail'),
    url(r'^customer/(?P<pk>[0-9]+)/session/create/$',
        views.SessionCreateView.as_view(),
        name='session_create'),
    url(r'^session/(?P<pk>[0-9]+)/update/$',
        views.SessionUpdateView.as_view(),
        name='session_update'),
    url(r'^session//(?P<pk>[0-9]+)/delete/$',
        views.SessionDeleteView.as_view(),
        name='session_delete'),


]
