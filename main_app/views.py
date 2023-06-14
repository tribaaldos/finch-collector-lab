from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bike
from .forms import FillingForm
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bikes_index(request):
  # We pass data to a template very much like we did in Express!
  bikes = Bike.objects.all()
  filling_form = FillingForm()
  return render(request, 'bikes/index.html', {
    'bikes': bikes, 'filling_form': filling_form
  })
  
def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  filling_form = FillingForm()
  return render(request, 'bikes/detail.html', {
    'bike': bike, 'filling_form': filling_form
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
  
def add_filling(request, bike_id):
  # create a ModelForm instance using the data in request.POST
  form = FillingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_filling = form.save(commit=False)
    new_filling.bike_id = bike_id
    new_filling.save()
  return redirect('detail', bike_id=bike_id)