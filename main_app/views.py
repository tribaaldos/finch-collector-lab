from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  return render(request, 'bikes/detail.html', {
    'bike': bike
    })
class BikeCreate(CreateView):
  model = Bike
  fields = '__all__' #['name','breed','description','age']
  
class BikeUpdate(UpdateView):
  model = Bike
  fields = ['model', 'description', 'year']

class BikeDelete(DeleteView):
  model = Bike
  success_url = '/bikes'