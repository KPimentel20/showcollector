from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('shows/', views.shows_index, name='index'),
  #route for shows index
  path('shows/<int:show_id>/', views.shows_detail, name='detail'),
  # new route used to show a form and create a cat
  path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
  # Add the new routes below
  path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
  path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
  path('shows/<int:show_id>/add_streamingservice/', views.add_streamingservice, name='add_streamingservice'),
]
