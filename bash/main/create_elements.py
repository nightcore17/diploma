import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
django.setup()

from main.models import RefrigerationElement

# Очищаем старые элементы
RefrigerationElement.objects.all().delete()

# Все элементы с координатами как на твоей схеме
elements = [
    # КР (кристаллизаторы)
    ("КР-6", "kp", "normal", -18, 0, 50, 130, 75, 45, "rect"),
    ("КР-7", "kp", "normal", -22, 0, 50, 190, 75, 45, "rect"),
    ("КР-8", "kp", "normal", -20, 0, 50, 250, 75, 45, "rect"),
    ("КР-9", "kp", "normal", -24, 0, 50, 310, 75, 45, "rect"),
    ("КР-10", "kp", "normal", -19, 0, 50, 370, 75, 45, "rect"),
    ("КР-10а", "kp", "normal", -21, 0, 50, 430, 75, 45, "rect"),
    
    # РД
    ("РД-1", "rd", "normal", 0, 0, 160, 190, 75, 45, "rect"),
    ("РД-2", "rd", "normal", 0, 0, 270, 190, 75, 45, "rect"),
    
    # ОЖ
    ("ОЖ-1", "oz", "normal", -5, 0, 270, 130, 60, 60, "circle"),
    ("ОЖ-2", "oz", "normal", -6, 0, 270, 60, 60, 60, "circle"),
    
    # Т (теплообменники)
    ("Т-27", "t", "normal", -12, 0, 160, 310, 110, 45, "wide"),
    ("Т-27а", "t", "normal", -13, 0, 160, 370, 110, 45, "wide"),
    ("Т-27б", "t", "normal", -14, 0, 160, 430, 110, 45, "wide"),
    ("Т-27в", "t", "normal", -15, 0, 160, 490, 110, 45, "wide"),
    
    # АДК (компрессоры)
    ("АДК-3", "adk", "normal", 3, 0, 450, 80, 75, 45, "rect"),
    ("АДК-2", "adk", "normal", 2, 0, 580, 80, 75, 45, "rect"),
    ("АДК-1", "adk", "normal", 1, 0, 710, 80, 75, 45, "rect"),
    
    # ПС (промсосуды)
    ("ПС-3", "ps", "normal", 0, 2.3, 450, 190, 60, 90, "vessel"),
    ("ПС-2", "ps", "normal", 0, 2.1, 580, 190, 60, 90, "vessel"),
    ("ПС-1", "ps", "normal", 0, 2.4, 710, 190, 60, 90, "vessel"),
    ("ПС-4", "ps", "normal", 0, 2.0, 1150, 190, 60, 90, "vessel"),
    
    # МО (маслоотделители)
    ("МО-3", "mo", "normal", 0, 0, 450, 430, 75, 45, "rect"),
    ("МО-2", "mo", "normal", 0, 0, 580, 430, 75, 45, "rect"),
    ("МО-1", "mo", "normal", 0, 0, 710, 430, 75, 45, "rect"),
    
    # АВО, ГЛ
    ("АВО-5.5а", "avo", "normal", 25, 0, 360, 380, 75, 45, "rect"),
    ("ГЛ-1", "gl", "normal", 0, 0, 490, 410, 75, 45, "rect"),
    
    # КТВ (конденсаторы)
    ("КТВ-1", "ktv", "normal", 0, 0, 450, 660, 75, 45, "rect"),
    ("КТВ-2", "ktv", "normal", 0, 0, 580, 660, 75, 45, "rect"),
    ("КТВ-3", "ktv", "normal", 0, 0, 710, 660, 75, 45, "rect"),
    ("КТВ-4", "ktv", "normal", 0, 0, 840, 660, 75, 45, "rect"),
    ("КТВ-5", "ktv", "normal", 0, 0, 970, 660, 75, 45, "rect"),
    
    # ДАО-550
    ("ДАО-550", "dao", "normal", -32, 0, 950, 130, 160, 160, "big"),
    
    # РЛ (ресиверы линейные)
    ("РЛ-1", "rl", "normal", -4, 0, 1150, 370, 110, 45, "wide"),
    ("РЛ-2", "rl", "normal", -5, 0, 1150, 430, 110, 45, "wide"),
    ("РЛ-3", "rl", "normal", -6, 0, 1150, 490, 110, 45, "wide"),
    ("РЛ-4", "rl", "normal", -7, 0, 1050, 620, 260, 120, "rect"),
]

# Создаём элементы
for name, e_type, status, temp, press, x, y, w, h, shape in elements:
    RefrigerationElement.objects.create(
        name=name,
        element_type=e_type,
        status=status,
        temperature=temp,
        pressure=press,
        pos_x=x,
        pos_y=y,
        width=w,
        height=h,
        shape=shape,
        description=f"{name} - элемент схемы холодильного отделения"
    )

print(f"✅ Создано {len(elements)} элементов!")
print("Все элементы добавлены в базу:")
for e in RefrigerationElement.objects.all():
    print(f"  - {e.name} ({e.element_type})")