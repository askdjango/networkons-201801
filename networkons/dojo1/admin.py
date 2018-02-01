from django.contrib import admin
from .models import Customer, Field


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)


class FieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latlng', 'status']

admin.site.register(Field, FieldAdmin)

