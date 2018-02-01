from django.contrib import admin
from .models import Customer, Field, Place


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)


class FieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latlng', 'status']
    list_display_links = ['name']
    list_editable = ['latlng']
    list_filter = ['status']
    actions = ['make_open', 'make_close']

    def make_open(self, request, queryset):
        count = queryset.update(status='open')
        self.message_user(request, '{}건을 열림상태로 변경했습니다.'.format(count))
    make_open.short_description = '열림 상태로 변경'

    def make_close(self, request, queryset):
        count = queryset.update(status='close')
        self.message_user(request, '{}건을 닫힘상태로 변경했습니다.'.format(count))

admin.site.register(Field, FieldAdmin)


class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)

