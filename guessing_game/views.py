from django.shortcuts import render
# Create your views here.
import random
import requests

def index(request):
    api_url = 'https://countriesnow.space/api/v0.1/countries/capital'
    response = requests.get(api_url)
    countries_data = response.json()
    countries = countries_data['data']
    random_country = random.choice(countries)
    print(random_country)

    return render(request, 'guessing_game/index.html', {'random_country': random_country})
