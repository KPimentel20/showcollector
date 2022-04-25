from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Show class & list and view function below the imports
from .models import Show

shows = [
  Show('Insecure', 'Comedy', 'Issa Rae', 2016),
  Show('Games of Thrones', 'Fantasy/Drama', 'Winter is Coming', 2011),
  Show('Watchmen', 'Science Fiction', 'Superhero Drama', 2019)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome</h1>')

def about(request):
    return render(request, 'about.html')
#Add a new view

def shows_index(request):
    shows = Show.objects.all()
    return render(request, 'shows/index.html', { 'shows': shows })

def shows_detail(request, show_id):
  show = Show.objects.get(id=show_id)
  return render(request, 'shows/detail.html', { 'show': show })