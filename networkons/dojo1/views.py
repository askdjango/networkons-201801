from django.shortcuts import render
from .models import Field


def field_list(request):
    qs = Field.objects.all()  # QuerySet
    return render(request, 'dojo1/field_list.html', {
        'field_list': qs,
    })

