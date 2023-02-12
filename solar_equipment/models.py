from django.db import models


# Create your models here.
class SolarPanel(models.Model):
    name = models.TextField(max_length=100, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def save(self, *args, **kwargs):
        print("saving")
        super().save(*args, **kwargs)
