from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse
from .models import Show
from .forms import StreamingServiceForm


class ShowCreate(CreateView):
    model = Show
    fields = '__all__'
    success_url = '/shows/'

class ShowUpdate(UpdateView):
  model = Show
  # Let's disallow the renaming of a show by excluding the name field!
  fields = ['genre', 'description', 'releaseyear']
  success_url = '/shows/'

class ShowDelete(DeleteView):
  model = Show
  success_url = '/shows/'

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

def shows_detail(request, show_id):
    show = Show.objects.get(id=show_id)
    streamingservice_form = StreamingServiceForm()

    return render(request, 'shows/detail.html', {
        'show': show, 'streamingservice_form': streamingservice_form
    })

def add_streamingservice(request, show_id):
  pass

def add_streamingservice(request, show_id):
  # create a ModelForm instance using the data in request.POST
  form = StreamingServiceForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_streamingservice = form.save(commit=False)
    new_streamingservice.show_id = show_id
    new_streamingservice.save()
  return redirect('detail', show_id=show_id)