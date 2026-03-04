from django.shortcuts import render, redirect, get_object_or_404
from .models import Apparatus

def index(request):
    # Прогноз погоды на неделю
    forecast_data = [
        {'day': 'Пн', 'temp': -10, 'cond': 'Ясно'},
        {'day': 'Вт', 'temp': -12, 'cond': 'Снег'},
        {'day': 'Ср', 'temp': -8, 'cond': 'Облачно'},
        {'day': 'Чт', 'temp': -5, 'cond': 'Метель'},
        {'day': 'Пт', 'temp': -7, 'cond': 'Ясно'},
        {'day': 'Сб', 'temp': -15, 'cond': 'Ясно'},
        {'day': 'Вс', 'temp': -13, 'cond': 'Снег'},
    ]
    
    context = {
        'unit_load': 125.5,
        'temp_out': -12,
        'brigade_name': 'Бригада №4',
        'master_name': 'Иванов И.И.',
        'forecast': forecast_data,
    }
    return render(request, 'main/index.html', context)

def cooling_section(request):
    apparatus_list = Apparatus.objects.all()
    # Авто-наполнение базы при первом запуске
    if not apparatus_list.exists():
        Apparatus.objects.create(position="Х-1", name="Первичный холодильник", pressure=4.2, temperature=45)
        Apparatus.objects.create(position="Х-2", name="Вторичный холодильник", pressure=3.8, temperature=38)
        apparatus_list = Apparatus.objects.all()
    
    return render(request, 'main/scheme.html', {'apparatus_list': apparatus_list})

def update_params(request):
    if request.method == "POST":
        app_id = request.POST.get('app_id')
        apparatus = get_object_or_404(Apparatus, id=app_id)
        apparatus.pressure = request.POST.get('pressure')
        apparatus.temperature = request.POST.get('temperature')
        apparatus.save()
    return redirect('cooling_section')