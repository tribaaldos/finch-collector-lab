from django.db import models
from django.urls import reverse

FUELS = (
    ('D', 'Diesel'),
    ('G', 'Gasoline'),
    ('L', 'Gasoil')

)


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
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bike_id': self.id})

class Filling(models.Model):
  date = models.DateField('filling date')
  fuel = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=FUELS,
    # set the default value for meal to be 'B'
    default=FUELS[0][0]
  )
  #create a bike_id FK 
  bike = models.ForeignKey( Bike, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_fuel_display()} on {self.date}"
    
  class Meta:
      ordering = ['-date']