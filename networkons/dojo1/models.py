import os
import re
import pandas as pd
from django import forms
from django.db import models


def validate_phone(phone):
    # phone # 입력받은 문자열

    if not re.match(r'01[016789][1-9]\d{7}', phone):
        raise forms.ValidationError('전화번호를 입력해주세요.')


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13,
                             validators=[validate_phone])


class Field(models.Model):
    name = models.CharField(max_length=100, verbose_name='이름')
    # position = models.PointField()
    latlng = models.CharField(max_length=50,
            help_text='"위도,경도" 포맷으로 입력해주세요.')
    status = models.CharField(
            max_length=10,
            choices=[
                ['open', '열림'],
                ['close', '닫힘'],
            ],
            default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Place(models.Model):
    voc_type = models.CharField(max_length=20)
    try_nm = models.CharField(max_length=2)
    sgg_nm = models.CharField(max_length=3)
    emd_nm = models.CharField(max_length=5)
    latitute = models.FloatField()
    longitude = models.FloatField()
    occr_date = models.DateField()
    photo = models.ImageField(blank=True)


class Record(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='%Y%m%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_pandas_dataframe(self):
        ext = os.path.splitext(self.file.path)[1].lower()

        if ext == '.csv':
            return pd.read_csv(self.file.path)
        elif ext in ['.xls', '.xlsx']:
            return pd.read_excel(self.file.path)

        return None
