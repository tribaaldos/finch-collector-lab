from django.shortcuts import render
from .models import Bike
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
  # We pass data to a template very much like we did in Express!
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {
    'bikes': bikes
  })
  
def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  return render(request, 'bikes/detail.html', { 'bike': bike})