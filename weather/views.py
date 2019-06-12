import random
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.shortcuts import render
import requests #to make api call
from .models import City, Feedback, Message
from .forms import CityForm, FeedbackForm, MessageForm

# Create your views here.

def index(request):
    
    #loc = '30.7343,76.7933'
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=8f100941286957285632fd852f871cb8'
    cities = City.objects.all()[City.objects.count()-3::-1] # return all the cities in the database
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # inserts city name to the database
        
    form = CityForm()
    
    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city.name)).json()
        
        # to generate random object from the database
        qs = Message.objects.all()
        random_message = random.choice(qs)
        
        weather = {'city': city_weather['city']['name'], # city
                   #'message': css.msg(),
                   'temperature' : round(city_weather['list'][0]['main']['temp']),
                   'icon' : city_weather['list'][0]['weather'][0]['icon'],
                   'description' : city_weather['list'][0]['weather'][0]['description'],
                   
                   'message': random_message.message,
                   'temp_min':  round(city_weather['list'][0]['main']['temp_min']),
                   'temp_max':  round(city_weather['list'][0]['main']['temp_max']),
                   'wind_speed': city_weather['list'][0]['wind']['speed'],
                   }
        weather_data.append(weather)
        
    context = {'weather_data' : weather_data, 'form' : form}
    
    return render(request, 'practice.html', context)

def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = FeedbackForm()
    context = {'form': form, 'title': 'Feedback'}
    return render(request, 'form.html', context)

def info_page(request):
    return render(request, 'i_page.html')
 
@login_required
def feedbacklist(request):
    qs = Feedback.objects.all()
    context = {'feedbacks': qs}
    return render(request, 'feedbacklist.html', context)

def add_message(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = MessageForm()
    context = {'form': form, 'title': 'Add Message'}
    return render(request, 'form.html', context)







