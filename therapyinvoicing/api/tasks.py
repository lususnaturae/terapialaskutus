from __future__ import absolute_import
from celery import shared_task
from django.db.models import Sum, F
from django.utils import timezone


@shared_task
def clean_and_init_api_monthlyrevenue():
    from .models import MonthlyRevenue
    # clear model MonthlyRevenue
    MonthlyRevenue.objects.all().delete()
    # Populate table starting from 2015 to current year
    currentyear = timezone.now().year
    t=0
    for y in range(2015, currentyear+1):
        for m in range(1, 13):
            mr = MonthlyRevenue(
                year = '{0:04d}'.format(y),
                month = '{0:02d}'.format(m),
                customerRevenue = 0.0,
                kelaRevenue=0.0
            )
            mr.save()
            t += 1
    x=1

# FIXME: Change update_api_monthlyrevenue(), so that it will not update new data everytime when api is called, but only after new invoices are created
@shared_task
def update_api_monthlyrevenue():
    from .models import MonthlyRevenue
    from ..customerinvoicing.models import InvoiceLineItem
    from ..kelainvoicing.models import KelaInvoiceLineItem
    # init data in MontlyRevenue
    clean_and_init_api_monthlyrevenue()
    # get revenue invoiced from customer
    mrlist = MonthlyRevenue.objects.all().order_by('year', 'month')
    for mr in mrlist:
        crlist = InvoiceLineItem.objects.filter(date__year= int(mr.year), date__month=int(mr.month))
        if crlist.exists():
            crsum = crlist.aggregate(customerrevenue=Sum(F('sessionprice') - F('sessionpriceKelaRefund')))
            mr.customerRevenue = crsum['customerrevenue']
        krlist = KelaInvoiceLineItem.objects.filter(date__year= int(mr.year), date__month=int(mr.month))
        if krlist.exists():
            krsum = krlist.aggregate(kelarevenue=Sum('sessionpriceKelaRefund'))
            mr.kelaRevenue = krsum['kelarevenue']
        mr.save()

