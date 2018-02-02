import os
import pandas as pd
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from .models import Field, Place


def field_list(request):
    qs = Field.objects.all()  # QuerySet
    return render(request, 'dojo1/field_list.html', {
        'field_list': qs,
    })


def field_list2(request):
    # path = os.path.join(settings.BASE_DIR, '지도_mapping_실습.xlsx')
    # df = pd.read_excel(path)
    # df['addr'] = df['try_nm'] + ' ' + df['sgg_nm'] + ' ' + df['emd_nm']

    qs = Place.objects.all()

    q = request.GET.get('q', '')

    if q:
        qs = qs.filter(
            Q(try_nm__icontains=q) |
            Q(sgg_nm__icontains=q) |
            Q(emd_nm__icontains=q))

    return render(request, 'dojo1/field_list2.html', {
        # 'df': df,
        'place_list': qs,
        'q': q,
        'NAVER_MAP_API_KEY': settings.NAVER_MAP_API_KEY,
    })

