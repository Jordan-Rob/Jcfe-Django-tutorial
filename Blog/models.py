from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    name = models.CharField(max_length=120)
    article = models.TextField(blank=False, null=True)
    author = models.CharField(max_length=120)

    def get_absolute_url(self):
        return f"/Blog/article/{self.id}/"
        # return reverse("Blog:article", kwargs={"id": self.id})
