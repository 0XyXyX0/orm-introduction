from django.db import models

class Nigga(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.price}$"