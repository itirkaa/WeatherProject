# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, Textarea
from .models import City, Feedback, Message

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }
        
class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
        widgets = {
                'feedback': Textarea(attrs={'rows':2, 'cols':20}),
        }

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'message']
        widgets = {
                'message': Textarea(attrs={'rows':4, 'cols':20}),
        }