from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Show class & list and view function below the imports
class Show:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, genre, description, releaseyear):
    self.name = name
    self.genre = genre
    self.description = description
    self.releaseyear = releaseyear

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
    return render(request, 'shows/index.html', { 'shows': shows })