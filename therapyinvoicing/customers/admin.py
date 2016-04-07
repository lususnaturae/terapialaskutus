from django.contrib import admin
from .models import Customer, Session, CompanyProfile


class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['firstName',  'lastName', 'ssn', 'address', 'zipCode', 'city', 'status',
              'therapyCategory', 'sessionprice', 'sessionpriceKelaRefund']
    fields = ['firstName',  'lastName', 'ssn', 'address', 'zipCode', 'city',  'telephone', 'email', 'status',
              'therapyCategory', 'sessionprice', 'sessionpriceKelaRefund']
    list_filter = ['status']

    class Meta:
         model = Customer


class SessionAdmin(admin.ModelAdmin):
    fields = ['date',  'time',  'sessionInvoiceType', 'kelaInvoiceType',
              'sessionType', 'sessionDone', 'kelaInvoiced', 'customerInvoiced', 'sessionprice',
              'sessionpriceKelaRefund'
              ]
    empty_value_display = '-empty-'
    list_display = ['date',  'time',  'sessionDone', 'customer']

    class Meta:
         model = Session


class CompanyProfileAdmin(admin.ModelAdmin):
    class Meta:
         model = CompanyProfile

# register models
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin)

