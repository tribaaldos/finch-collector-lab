from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })
  
finches = [
{'name': 'Ahmed', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
{'name': 'Jason', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
{'name': 'Angel', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
{'name': 'Clem', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]