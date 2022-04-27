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
  path('shows/<int:show_id>/assoc_creator/<int:creator_id>/', views.assoc_creator, name='assoc_creator'),
  path('creators/', views.CreatorList.as_view(), name='creators_index'),
  path('creators/<int:pk>/', views.CreatorDetail.as_view(), name='creators_detail'),
  path('creators/create/', views.CreatorCreate.as_view(), name='creators_create'),
  path('creators/<int:pk>/update/', views.CreatorUpdate.as_view(), name='creators_update'),
  path('creators/<int:pk>/delete/', views.CreatorDelete.as_view(), name='creators_delete'),
]