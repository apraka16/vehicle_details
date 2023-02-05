from django.db import models

# Create your models here.
class NewVehicle(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    year = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return f"{self.make} {self.model}"