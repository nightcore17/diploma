from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Brigade, RefrigerationElement
import json

def index(request):
    # Получаем все элементы
    elements = RefrigerationElement.objects.all()
    
    # Получаем первую бригаду или создаем тестовую
    brigade = Brigade.objects.first()
    if not brigade:
        brigade = Brigade.objects.create(
            name="Бригада №1",
            leader="Иванов И.И.",
            is_working=True
        )
    
    # Подготовка данных для JSON
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
    
    # Основные показатели
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
    }
    
    return render(request, 'main/index.html', context)

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
def element_detail(request, element_id):
    element = RefrigerationElement.objects.get(id=element_id)
    return render(request, 'main/element_detail.html', {'element': element})
def full_schema(request):
    return render(request, 'main/full_schema.html')