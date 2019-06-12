from django.contrib import admin
from .models import City, Feedback, Message

# Register your models here.
admin.site.register(City)
admin.site.register(Feedback)
admin.site.register(Message)