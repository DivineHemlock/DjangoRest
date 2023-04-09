from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=100.00)
