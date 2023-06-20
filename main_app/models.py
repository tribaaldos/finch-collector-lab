from django.db import models
from django.urls import reverse
from datetime import date

FUELS = (
  ('G', 'Gasoline'),
  ('L', 'Gasoil'),
  ('D', 'Diesel'),
)


# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Bike(models.Model):
  brand = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  # Create a M:M relationship with Toy
  # toys is the Related Manager
  toys = models.ManyToManyField(Toy)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.brand} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'bike_id': self.id})

  def filled_for_today(self):
    return self.filling_set.filter(date=date.today()).count() >= len(FUELS)


class Filling(models.Model):
  date = models.DateField('Filling Date')
  fuel = models.CharField(
    max_length=1,
    choices=FUELS,
    default=FUELS[0][0]
  )
  # Create a bike_id FK
  bike = models.ForeignKey(
    Bike,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_fuel_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
