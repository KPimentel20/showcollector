from django.forms import ModelForm
from .models import StreamingService

class StreamingServiceForm(ModelForm):
  class Meta:
    model = StreamingService
    fields = ['date', 'channel']