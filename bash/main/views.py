from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import RefrigerationElement, Brigade, WeatherForecast, RawMaterial, RawMaterialLoad, ShiftLog, Order
import json
import random
from datetime import date, timedelta

def get_weather_forecast():
    today = date.today()
    if WeatherForecast.objects.count() == 0:
        for i in range(7):
            WeatherForecast.objects.create(
                date=today + timedelta(days=i),
                temperature_day=20,
                temperature_night=10,
                condition="Ясно",
                humidity=60,
                wind_speed=3,
                icon="☀️"
            )
    return WeatherForecast.objects.all().order_by('date')[:7]

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
            'element_type': e.element_type,
            'temperature': round(e.temperature, 1),
            'ammonia_temp': round(e.ammonia_temp, 1),
            'pressure': round(e.pressure, 1),
            'level': round(e.level, 1),
            'discharge_temp_stage1': round(e.discharge_temp_stage1, 1),
            'discharge_temp_stage2': round(e.discharge_temp_stage2, 1),
            'status': e.status,
            'pos_x': e.pos_x,
            'pos_y': e.pos_y,
        })
    
    total_elements = elements.count()
    avg_temp = 0
    alarm_count = 0
    stopped_count = elements.filter(status='stopped').count()
    working_count = elements.filter(status='normal').count()
    
    if total_elements > 0:
        avg_temp = sum([e.temperature for e in elements]) / total_elements
        alarm_count = elements.filter(status='alarm').count()
    
    context = {
        'elements': elements,
        'elements_json': json.dumps(elements_list),
        'brigade': brigade,
        'total_elements': total_elements,
        'working_count': working_count,
        'stopped_count': stopped_count,
        'avg_temperature': round(avg_temp, 1),
        'alarm_count': alarm_count,
        'forecasts': forecasts,
    }
    return render(request, 'main/index.html', context)

def element_detail(request, element_id):
    element = get_object_or_404(RefrigerationElement, id=element_id)
    return render(request, 'main/element_detail.html', {'element': element})

def element_data(request, element_id):
    element = get_object_or_404(RefrigerationElement, id=element_id)
    data = {
        'id': element.id,
        'name': element.name,
        'element_type': element.element_type,
        'temperature': round(element.temperature, 1),
        'ammonia_temp': round(element.ammonia_temp, 1),
        'pressure': round(element.pressure, 1),
        'level': round(element.level, 1) if element.level else 50,
        'discharge_temp_stage1': round(element.discharge_temp_stage1, 1),
        'discharge_temp_stage2': round(element.discharge_temp_stage2, 1),
        'status': element.status,
    }
    return JsonResponse(data)

def full_schema(request):
    elements = RefrigerationElement.objects.all()
    for e in elements:
        e.temperature = round(e.temperature, 1)
        e.ammonia_temp = round(e.ammonia_temp, 1)
        e.pressure = round(e.pressure, 1)
        e.level = round(e.level, 1)
        e.discharge_temp_stage1 = round(e.discharge_temp_stage1, 1)
        e.discharge_temp_stage2 = round(e.discharge_temp_stage2, 1)
    return render(request, 'main/full_schema.html', {'elements': elements})

def weather_forecast(request):
    forecasts = get_weather_forecast()
    return render(request, 'main/weather.html', {'forecasts': forecasts})

def analytics(request):
    materials = RawMaterial.objects.all()
    loads = RawMaterialLoad.objects.all().order_by('-created_at')[:20]
    total_loaded = sum(load.volume for load in RawMaterialLoad.objects.filter(status='completed'))
    active_loads = RawMaterialLoad.objects.filter(status='in_progress').count()
    completed_today = RawMaterialLoad.objects.filter(status='completed', end_time__date=date.today()).count()
    materials_count = materials.count()
    
    context = {
        'materials': materials,
        'loads': loads,
        'total_loaded': round(total_loaded, 1),
        'active_loads': active_loads,
        'completed_today': completed_today,
        'materials_count': materials_count,
    }
    return render(request, 'main/analytics.html', context)

def shift_log(request):
    brigade = Brigade.objects.first()
    logs = ShiftLog.objects.all().order_by('-date', '-time_from')[:50]
    return render(request, 'main/journal.html', {'brigade': brigade, 'logs': logs})

def orders(request):
    brigade = Brigade.objects.first()
    all_orders = Order.objects.all().order_by('-created_at')
    active_orders = all_orders.filter(status='active').count()
    in_progress_orders = all_orders.filter(status='in_progress').count()
    completed_orders = all_orders.filter(status='completed').count()
    orders_list = all_orders[:50]
    
    context = {
        'brigade': brigade,
        'orders': orders_list,
        'active_orders': active_orders,
        'in_progress_orders': in_progress_orders,
        'completed_orders': completed_orders,
    }
    return render(request, 'main/orders.html', context)

@csrf_exempt
def update_element(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element = RefrigerationElement.objects.get(id=data.get('id'))
            if 'temperature' in data: element.temperature = round(float(data['temperature']), 1)
            if 'ammonia_temp' in data: element.ammonia_temp = round(float(data['ammonia_temp']), 1)
            if 'pressure' in data: element.pressure = round(float(data['pressure']), 1)
            if 'level' in data: element.level = round(float(data['level']), 1)
            if 'discharge_temp_stage1' in data: element.discharge_temp_stage1 = round(float(data['discharge_temp_stage1']), 1)
            if 'discharge_temp_stage2' in data: element.discharge_temp_stage2 = round(float(data['discharge_temp_stage2']), 1)
            if 'status' in data: element.status = data['status']
            element.save()
            return JsonResponse({'success': True, 'message': f'{element.name} обновлен'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})

@csrf_exempt
def update_level(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element = RefrigerationElement.objects.get(id=data.get('id'))
            element.level = round(float(data.get('level', 50)), 1)
            element.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})

@csrf_exempt
def toggle_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element = RefrigerationElement.objects.get(id=data.get('id'))
            action = data.get('action')
            if action == 'stop': element.status = 'stopped'
            elif action == 'start': element.status = 'normal'
            element.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})

@csrf_exempt
def random_update(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            element = RefrigerationElement.objects.get(id=data.get('id'))
            delta = float(data.get('delta', 0))
            if element.status != 'stopped':
                element.temperature = round(element.temperature + delta, 1)
                if element.element_type in ['rd', 'rl', 'ps', 'ms', 'ktv']:
                    element.level = max(0, min(100, round(element.level + random.uniform(-3, 3), 1)))
                if element.element_type == 'compressor':
                    element.discharge_temp_stage1 = round(element.discharge_temp_stage1 + random.uniform(-1, 1), 1)
                    element.discharge_temp_stage2 = round(element.discharge_temp_stage2 + random.uniform(-1, 1), 1)
                element.save()
                return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False})

def get_data(request):
    elements = RefrigerationElement.objects.all()
    data = []
    for e in elements:
        data.append({
            'id': e.id, 'name': e.name, 'element_type': e.element_type,
            'temperature': round(e.temperature, 1), 'ammonia_temp': round(e.ammonia_temp, 1),
            'pressure': round(e.pressure, 1), 'level': round(e.level, 1),
            'discharge_temp_stage1': round(e.discharge_temp_stage1, 1),
            'discharge_temp_stage2': round(e.discharge_temp_stage2, 1),
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