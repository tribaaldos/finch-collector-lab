from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bike, Toy
from .forms import FillingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bikes_index(request):
  bikes = Bike.objects.all()
  return render(request, 'bikes/index.html', {
    'bikes': bikes
  })

def bikes_detail(request, bike_id):
  bike = Bike.objects.get(id=bike_id)
  # First, create a list of the toy ids that the bike DOES have
  id_list = bike.toys.all().values_list('id')
  # Query for the toys that the bike doesn't have
  # by using the exclude() method vs. the filter() method
  toys_bike_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # instantiate FillingForm to be rendered in detail.html
  filling_form = FillingForm()
  return render(request, 'bikes/detail.html', {
    'bike': bike, 'filling_form': filling_form,
    'toys': toys_bike_doesnt_have
  })

class BikeCreate(CreateView):
  model = Bike
  fields = ['brand', 'model', 'description', 'year']

class BikeUpdate(UpdateView):
  model = Bike
  fields = ['model', 'description', 'year']

class BikeDelete(DeleteView):
  model = Bike
  success_url = '/bikes'

def add_filling(request, bike_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = FillingForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # bike_id FK.
    new_filling = form.save(commit=False)
    new_filling.bike_id = bike_id
    new_filling.save()
  return redirect('detail', bike_id=bike_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, bike_id, toy_id):
  Bike.objects.get(id=bike_id).toys.add(toy_id)
  return redirect('detail', bike_id=bike_id)

def unassoc_toy(request, bike_id, toy_id):
  Bike.objects.get(id=bike_id).toys.remove(toy_id)
  return redirect('detail', bike_id=bike_id)
