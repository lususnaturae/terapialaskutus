import datetime
import random
import time
from django.utils.translation import ugettext_lazy as _
from braces.views import GroupRequiredMixin
from django.views.generic import TemplateView
from ..api.models import MonthlyRevenue
from django.shortcuts import render_to_response


class MonthlyReportView(GroupRequiredMixin, TemplateView):
    group_required = u'therapist'
    raise_exception = True
    template_name = "reporting/monthlyrevenue.html"

    def get_context_data(self, **kwargs):
        context = super(MonthlyReportView, self).get_context_data(**kwargs)

        years = MonthlyRevenue.objects.order_by('year').values('year').distinct()
        if years.exists():
            yearlist = []
            for y in years:
                yearlist.append(y['year'])
            context['yearlist'] = yearlist
            selectedyear = yearlist[-1]
            context['selectedyear'] = selectedyear
            context['nodataalert'] = False
        else:
            context['nodataalert'] = True
        context['reporttitle'] = _("Liikevaihto")
        return context


class RevenueReportView(GroupRequiredMixin, TemplateView):
    group_required = u'therapist'
    raise_exception = True
    template_name = "reporting/revenuereport.html"

    def get_context_data(self, **kwargs):
        context = super(RevenueReportView, self).get_context_data(**kwargs)
        context['reporttitle'] = _("Liikevaihto NVD3 chart")
        #select year
        if 'year' in kwargs:
            year = kwargs['year']
        monthlist = MonthlyRevenue.objects.filter(year = '2015').order_by('month')
        xdata = []
        for m in monthlist:
            xdata.append(m.month)

        ydata = []
        for r in monthlist:
            ydata.append(r.customerRevenue + r.kelaRevenue)
        color_list = ["#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF","#68B3AF"]
        extra_serie1 = {"tooltip": {"y_start": "xx", "y_end": " cal"},
                        'color': '#68B3AF',
                        'color_list': color_list,
                        'category20': '#68B3AF'}
        chartdata = {
            'x': xdata,
            'name1': 'Euro',
            'y1': ydata,
            'extra1': extra_serie1,


        }
        charttype = "discreteBarChart"
        chartcontainer = 'discretebarchart_container'  # container name
        context['charttype'] = charttype
        context['chartdata'] = chartdata
        context['chartcontainer'] = chartcontainer
        context['extra'] ={
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': False,
                'showLegend': True,
            'colorCategory': 'category10',

        }
        return context


def demo_discretebarchart_with_date(request):
    """
    discretebarchart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 10

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {
        'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
    }
    charttype = "discreteBarChart"
    chartcontainer = 'discretebarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d-%b',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('reporting/discretebarchart_with_date.html', data)
