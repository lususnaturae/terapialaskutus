from django.contrib import admin
from .models import Invoice, InvoiceLineItem, InvoiceCustomer, InvoiceCompanyProfile


class InvoiceAdmin(admin.ModelAdmin):
    class Meta:
         model = Invoice


class InvoiceLineItemAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    class Meta:
         model = InvoiceLineItem


class InvoiceCustomerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    class Meta:
         model = InvoiceCustomer


class InvoiceCompanyProfileAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    class Meta:
         model = InvoiceCompanyProfile

# Register models
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceLineItem, InvoiceLineItemAdmin)
admin.site.register(InvoiceCustomer, InvoiceCustomerAdmin)
admin.site.register(InvoiceCompanyProfile, InvoiceCompanyProfileAdmin)
