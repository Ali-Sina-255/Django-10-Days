from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title
