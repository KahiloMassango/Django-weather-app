from django.shortcuts import render, redirect
from dotenv import load_dotenv
import os
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required 
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, location
import requests

load_dotenv()

def login_view(request):
    if request.user.is_authenticated:
        return redirect("weather:home")
    if request.method == 'GET':
        form = LoginForm
        return render(request, 'login.html', {'form':form})
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("weather:home")
        else:
            return HttpResponse('crendeciais erradas')

@require_GET
def register_view(request):
    if request.user.is_authenticated:
        return redirect("weather:home")
    else:
        form = RegisterForm
        return render(request, 'register.html', {'form': form})
       
@require_POST
def create_user(request):
    if not request.POST:
        raise Http404()
    
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('weather:login') 
    return redirect('weather:register')       

def logout_view(request):
    logout(request)
    return redirect('weather:login')

@login_required
def home_view(request):    
    cities = location.objects.filter(user=request.user)
    token = os.environ.get('API_TOKEN')
    
    weather_data = []

    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=en&units=metric&appid={token}"
        r = requests.get(url.format(city)).json()
        
        
        city_weather = {    
            'id': city.id,
            'city': city,
            'temp': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'weather_icon': r['weather'][0]['description'].replace(" ", ""), 
        }

        weather_data.append(city_weather)

    context = {'weather_data':weather_data}
    return render(request, 'home.html', context)

def get_info(request):
    city_name = request.POST['city']
    city = location(location_name=city_name, user=request.user)
    city.save()
    return redirect('weather:home') 

def delete_view(request, pk):
    obj = location.objects.get(pk=pk)
    obj.delete()
    return redirect('weather:home') 