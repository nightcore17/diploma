import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
django.setup()

from main.models import Employee, Brigade
from datetime import time, date

print("=" * 60)
print("ДОБАВЛЕНИЕ БРИГАД И СОТРУДНИКОВ")
print("=" * 60)

# Проверяем, есть ли уже сотрудники
if Employee.objects.count() > 0:
    print(f"\n⚠️ В базе уже есть {Employee.objects.count()} сотрудников.")
    user_input = input("Хотите добавить новых сотрудников? (y/n): ")
    if user_input.lower() != 'y':
        print("Пропускаем создание сотрудников.")
    else:
        Employee.objects.all().delete()
        print("Старые сотрудники удалены.")
        create_employees = True
else:
    create_employees = True

if create_employees:
    # Сотрудники для 4 бригад
    employees_data = [
        # Бригада 1 (дневная)
        ("Петров И.И.", "senior_operator", "+7-999-111-2233", date(2020, 1, 10)),
        ("Сидоров А.А.", "refrigeration_operator", "+7-999-111-2234", date(2021, 3, 15)),
        ("Кузнецов В.В.", "pump_operator", "+7-999-111-2235", date(2022, 5, 20)),
        ("Смирнова Е.В.", "regeneration_operator", "+7-999-111-2236", date(2021, 8, 10)),
        ("Михайлов Д.Д.", "filter_operator", "+7-999-111-2237", date(2023, 1, 5)),
        # Бригада 2 (дневная)
        ("Иванов И.И.", "senior_operator", "+7-999-222-3344", date(2019, 6, 10)),
        ("Козлов К.К.", "refrigeration_operator", "+7-999-222-3345", date(2020, 9, 15)),
        ("Новиков Н.Н.", "pump_operator", "+7-999-222-3346", date(2021, 11, 20)),
        ("Морозова М.М.", "regeneration_operator", "+7-999-222-3347", date(2022, 2, 10)),
        ("Волков В.В.", "filter_operator", "+7-999-222-3348", date(2022, 7, 5)),
        # Бригада 3 (ночная)
        ("Соколов С.С.", "senior_operator", "+7-999-333-4455", date(2020, 3, 10)),
        ("Лебедев Л.Л.", "refrigeration_operator", "+7-999-333-4456", date(2021, 5, 15)),
        ("Павлов П.П.", "pump_operator", "+7-999-333-4457", date(2021, 10, 20)),
        ("Егорова Е.Е.", "regeneration_operator", "+7-999-333-4458", date(2022, 4, 10)),
        ("Тимофеев Т.Т.", "filter_operator", "+7-999-333-4459", date(2023, 2, 5)),
        # Бригада 4 (ночная)
        ("Фёдоров Ф.Ф.", "senior_operator", "+7-999-444-5566", date(2019, 11, 10)),
        ("Яковлев Я.Я.", "refrigeration_operator", "+7-999-444-5567", date(2020, 12, 15)),
        ("Николаев Н.Н.", "pump_operator", "+7-999-444-5568", date(2021, 7, 20)),
        ("Александрова А.А.", "regeneration_operator", "+7-999-444-5569", date(2022, 9, 10)),
        ("Григорьев Г.Г.", "filter_operator", "+7-999-444-5570", date(2023, 3, 5)),
    ]
    
    print("\n📋 Создаём сотрудников...")
    employees = {}
    for name, position, phone, hire_date in employees_data:
        emp, created = Employee.objects.get_or_create(
            full_name=name,
            defaults={
                'position': position,
                'phone': phone,
                'hire_date': hire_date
            }
        )
        employees[name] = emp
        if created:
            print(f"  ✅ {name} - {emp.get_position_display()}")
        else:
            print(f"  ⚠️ {name} уже существует")
    
    print(f"\n✅ Сотрудников в базе: {Employee.objects.count()}")

# Проверяем бригады
if Brigade.objects.count() > 0:
    print(f"\n⚠️ В базе уже есть {Brigade.objects.count()} бригад.")
    user_input = input("Хотите добавить новые бригады? (y/n): ")
    if user_input.lower() != 'y':
        print("Пропускаем создание бригад.")
        create_brigades = False
    else:
        Brigade.objects.all().delete()
        print("Старые бригады удалены.")
        create_brigades = True
else:
    create_brigades = True

if create_brigades:
    # Получаем всех сотрудников
    employees = {emp.full_name: emp for emp in Employee.objects.all()}
    
    # Данные для 4 бригад
    brigades_data = [
        {
            'number': 1,
            'name': 'Дневная смена "Альфа"',
            'shift_start': time(8, 0),
            'shift_end': time(20, 0),
            'senior': "Петров И.И.",
            'refrigeration': "Сидоров А.А.",
            'pump': "Кузнецов В.В.",
            'regeneration': "Смирнова Е.В.",
            'filter': "Михайлов Д.Д.",
            'is_working': True,
        },
        {
            'number': 2,
            'name': 'Дневная смена "Бета"',
            'shift_start': time(8, 0),
            'shift_end': time(20, 0),
            'senior': "Иванов И.И.",
            'refrigeration': "Козлов К.К.",
            'pump': "Новиков Н.Н.",
            'regeneration': "Морозова М.М.",
            'filter': "Волков В.В.",
            'is_working': True,
        },
        {
            'number': 3,
            'name': 'Ночная смена "Гамма"',
            'shift_start': time(20, 0),
            'shift_end': time(8, 0),
            'senior': "Соколов С.С.",
            'refrigeration': "Лебедев Л.Л.",
            'pump': "Павлов П.П.",
            'regeneration': "Егорова Е.Е.",
            'filter': "Тимофеев Т.Т.",
            'is_working': False,
        },
        {
            'number': 4,
            'name': 'Ночная смена "Дельта"',
            'shift_start': time(20, 0),
            'shift_end': time(8, 0),
            'senior': "Фёдоров Ф.Ф.",
            'refrigeration': "Яковлев Я.Я.",
            'pump': "Николаев Н.Н.",
            'regeneration': "Александрова А.А.",
            'filter': "Григорьев Г.Г.",
            'is_working': False,
        },
    ]
    
    print("\n📋 Создаём бригады...")
    for data in brigades_data:
        brigade, created = Brigade.objects.get_or_create(
            number=data['number'],
            defaults={
                'name': data['name'],
                'shift_start': data['shift_start'],
                'shift_end': data['shift_end'],
                'senior_operator': employees.get(data['senior']),
                'refrigeration_operator': employees.get(data['refrigeration']),
                'pump_operator': employees.get(data['pump']),
                'regeneration_operator': employees.get(data['regeneration']),
                'filter_operator': employees.get(data['filter']),
                'is_working': data['is_working'],
            }
        )
        if created:
            print(f"  ✅ Бригада №{brigade.number} - {brigade.name}")
            print(f"     ⏰ Смена: {brigade.get_shift_display()}")
            print(f"     👤 Старший оператор: {brigade.senior_operator.full_name if brigade.senior_operator else 'Не назначен'}")
        else:
            print(f"  ⚠️ Бригада №{brigade.number} уже существует")
    
    print(f"\n✅ Бригад в базе: {Brigade.objects.count()}")

print("\n" + "=" * 60)
print("📊 ИТОГО:")
print(f"   👥 Сотрудников: {Employee.objects.count()}")
print(f"   🏢 Бригад: {Brigade.objects.count()}")
print("=" * 60)