from rest_framework.generics import ListAPIView
from braces.views import GroupRequiredMixin

from therapyinvoicing.api.tasks import update_api_monthlyrevenue
from .models import MonthlyRevenue
from .serializers import MonthlyRevenueSerializer


class MonthlyRevenueListView(GroupRequiredMixin, ListAPIView):
    group_required = u'therapist'
    raise_exception = True
    queryset = MonthlyRevenue.objects.all()
    serializer_class = MonthlyRevenueSerializer

    def get_queryset(self):
        # update data to model MonthlyRevenue
        update_api_monthlyrevenue()
        if 'year' in self.kwargs:
            selectedlist = MonthlyRevenue.objects.filter(year=self.kwargs['year']).order_by("year", "month")
        else:
            selectedlist = MonthlyRevenue.objects.all().order_by("year", "month")
        return selectedlist


