from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r'^monthlyrevenue/$',
        view=views.MonthlyReportView.as_view(),
        name='monthlyrevenue'),

]
