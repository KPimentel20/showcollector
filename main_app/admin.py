from django.contrib import admin

# Register your models here.
from .models import Show, StreamingService, Creator
admin.site.register(Show)
admin.site.register(StreamingService)
admin.site.register(Creator)