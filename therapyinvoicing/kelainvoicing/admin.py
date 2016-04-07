from django.contrib import admin
from .models import KelaStatement, KelaInvoice, KelaInvoiceLineItem, KelaInvoiceCustomer, KelaInvoiceCompanyProfile, KelaContactProfile


class KelaStatementAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaStatement


class KelaInvoiceAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaInvoice


class KelaInvoiceLineItemAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaInvoiceLineItem


class KelaInvoiceCustomerAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaInvoiceCustomer


class KelaInvoiceCompanyProfileAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaInvoiceCompanyProfile


class KelaContactProfileAdmin(admin.ModelAdmin):
    class Meta:
         model = KelaContactProfile


# register models
admin.site.register(KelaStatement, KelaStatementAdmin)
admin.site.register(KelaInvoice, KelaInvoiceAdmin)
admin.site.register(KelaInvoiceLineItem, KelaInvoiceLineItemAdmin)
admin.site.register(KelaInvoiceCustomer, KelaInvoiceCustomerAdmin)
admin.site.register(KelaInvoiceCompanyProfile, KelaInvoiceCompanyProfileAdmin)
admin.site.register(KelaContactProfile, KelaContactProfileAdmin)

