from django.urls import path
from . import views
	
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bikes/', views.bikes_index, name='index'),
  path('bikes/<int:bike_id>/', views.bikes_detail, name='detail'),
  path('bike/create/', views.BikeCreate.as_view(), name='bikes_create'),
  path('bikes/<int:pk>/update/', views.BikeUpdate.as_view(), name='bikes_update'),
  path('bikes/<int:pk>/delete/', views.BikeDelete.as_view(), name='bikes_delete'),
  path('bikes/<int:bike_id>/add_filling/', views.add_filling, name='add_filling'),
  path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
  path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

]