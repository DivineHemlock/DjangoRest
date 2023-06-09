from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=100.00)

    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
