from django.contrib import admin
from .models import Bike, Filling, Toy, Photo

# Register your models here.
admin.site.register(Bike)
admin.site.register(Filling)
admin.site.register(Toy)
admin.site.register(Photo)