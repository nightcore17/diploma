from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RefrigerationElement, Brigade, WeatherForecast
import json
import random
from datetime import date, timedelta
from django.db.models import Avg

def get_weather_forecast():
    today = date.today()
    if WeatherForecast.objects.count() < 7:
        WeatherForecast.objects.all().delete()
        conditions = [
            ("☀️", "Ясно", 20, 25),
            ("⛅", "Облачно", 15, 20),
            ("☁️", "Пасмурно", 10, 15),
            ("🌧️", "Дождь", 5, 10),
            ("❄️", "Снег", -5, 0),
            ("🌨️", "Снег с дождем", -2, 3),
            ("🌩️", "Гроза", 8, 12),
        ]
        for i in range(7):
            cond = random.choice(conditions)
            WeatherForecast.objects.create(
                date=today + timedelta(days=i),
                temperature_day=random.randint(cond[2], cond[3]),
                temperature_night=random.randint(cond[2]-5, cond[2]),
                condition=cond[1],
                humidity=random.randint(60, 90),
                wind_speed=random.randint(1, 8),
                icon=cond[0]
            )
    return WeatherForecast.objects.all()[:7]

def index(request):
    elements = RefrigerationElement.objects.all()
    brigade = Brigade.objects.first()
    if not brigade:
        brigade = Brigade.objects.create(name="Бригада №1", leader="Иванов И.И.", is_working=True)
    
    forecasts = get_weather_forecast()
    
    elements_list = []
    for e in elements:
        elements_list.append({
            'id': e.id,
            'name': e.name,
            'temperature': e.temperature,
            'pressure': e.pressure,
            'status': e.status,
            'pos_x': e.pos_x,
            'pos_y': e.pos_y,
        })
    
    total_elements = elements.count()
    avg_temp = 0
    alarm_count = 0
    if total_elements > 0:
        avg_temp = sum([e.temperature for e in elements]) / total_elements
        alarm_count = elements.filter(status='alarm').count()
    
    context = {
        'elements': elements,
        'elements_json': json.dumps(elements_list),
        'brigade': brigade,
        'total_elements': total_elements,
        'avg_temperature': round(avg_temp, 1),
        'alarm_count': alarm_count,
        'forecasts': forecasts,
    }
    return render(request, 'main/index.html', context)

def element_detail(request, element_id):
    element = get_object_or_404(RefrigerationElement, id=element_id)
    return render(request, 'main/element_detail.html', {'element': element})

def full_schema(request):
    elements = RefrigerationElement.objects.all()
    return render(request, 'main/full_schema.html', {'elements': elements})

def weather_forecast(request):
    forecasts = get_weather_forecast()
    return render(request, 'main/weather.html', {'forecasts': forecasts})

@csrf_exempt
def update_element(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element = RefrigerationElement.objects.get(id=data.get('id'))
            if 'temperature' in data:
                element.temperature = data['temperature']
            if 'pressure' in data:
                element.pressure = data['pressure']
            if 'status' in data:
                element.status = data['status']
            element.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Method not allowed'})

def get_data(request):
    elements = RefrigerationElement.objects.all()
    data = []
    for e in elements:
        data.append({
            'id': e.id,
            'temperature': e.temperature,
            'pressure': e.pressure,
            'status': e.status,
        })
    return JsonResponse({'elements': data})

@csrf_exempt
def update_weather(request):
    if request.method == 'POST':
        WeatherForecast.objects.all().delete()
        get_weather_forecast()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})