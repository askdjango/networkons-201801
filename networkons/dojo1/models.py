import re
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

