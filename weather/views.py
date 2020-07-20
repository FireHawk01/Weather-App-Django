from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=6ee90d6ab14055e4c56029b48d3cc7fa'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save() 
    form = CityForm()

    cities = City.objects.all()

    weather_data= []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
                }
        weather_data.append(city_weather)
    #print (city_weather)  
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)
