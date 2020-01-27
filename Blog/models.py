from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=120)
    article = models.TextField(blank=False, null=True)
    author = models.CharField(max_length=120)
