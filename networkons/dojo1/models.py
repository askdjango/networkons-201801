from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100)
    # position = models.PointField()
    latlng = models.CharField(max_length=50,
            help_text='"위도,경도" 포맷으로 입력해주세요.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

