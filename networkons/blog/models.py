from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class ZipCode(models.Model):
#     code = models.CharField(max_length=5, unique=True)

