from django.contrib import admin
from charge_management.models import Customer, Business


class CustomerShow(admin.ModelAdmin):
    list_display = ['name', 'business_name', 'charge', 'charge_time']


class BusinessDisplay(admin.ModelAdmin):
    list_display = ['business_name', 'credit']


admin.site.register(Customer, CustomerShow)
admin.site.register(Business, BusinessDisplay)