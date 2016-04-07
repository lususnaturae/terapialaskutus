from django.contrib import admin
from .models import MonthlyRevenue


class MonthlyRevenueAdmin(admin.ModelAdmin):
    class Meta:
         model = MonthlyRevenue

# Register models
admin.site.register(MonthlyRevenue, MonthlyRevenueAdmin)
