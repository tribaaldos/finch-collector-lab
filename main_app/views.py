import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bike, Toy, Photo
from .forms import FillingForm
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

def add_photo(request, bike_id):
  # photo-file maps to the "name" attr on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # Need a unique "key" (filename)
    # It needs to keep the same file extension
    # of the file that was uploaded (.png, .jpeg, etc.)
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, bike_id=bike_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', bike_id=bike_id)