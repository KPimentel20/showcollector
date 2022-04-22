from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  #route for shows index
  path('shows/', views.shows_index, name='index'),
]