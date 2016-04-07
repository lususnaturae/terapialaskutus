from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^monthlyrevenue/(?P<year>[0-9]+)/$',
        view=views.MonthlyRevenueListView.as_view(),
        name='monthlyrevenue_year_api'),
    url(regex=r'^monthlyrevenue/$',
        view=views.MonthlyRevenueListView.as_view(),
        name='monthlyrevenue_api'),

]
