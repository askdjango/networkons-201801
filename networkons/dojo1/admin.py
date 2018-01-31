from django.contrib import admin
from .models import Field


class FieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latlng']

admin.site.register(Field, FieldAdmin)

