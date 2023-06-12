from django.db import models

# Create your models here.
class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    #changing this instance method
    #does not impact the database, therefore
    #no migrations is necesssary
    def __str__(self):
        return f'{self.brand} ({self.id})'