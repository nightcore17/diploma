import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
import django
django.setup()

from main.models import RefrigerationElement

RefrigerationElement.objects.all().delete()

elements = [
    ("КР-6", "kp", -18, 0, 50, 130),
    ("КР-7", "kp", -22, 0, 50, 190),
    ("КР-8", "kp", -20, 0, 50, 250),
    ("КР-9", "kp", -24, 0, 50, 310),
    ("КР-10", "kp", -19, 0, 50, 370),
    ("КР-10а", "kp", -21, 0, 50, 430),
    ("РД-1", "rd", 0, 0, 160, 190),
    ("РД-2", "rd", 0, 0, 270, 190),
    ("ОЖ-1", "oz", -5, 0, 270, 130),
    ("ОЖ-2", "oz", -6, 0, 270, 60),
    ("Т-27", "t", -12, 0, 160, 310),
    ("Т-27а", "t", -13, 0, 160, 370),
    ("Т-27б", "t", -14, 0, 160, 430),
    ("Т-27в", "t", -15, 0, 160, 490),
    ("АДК-3", "compressor", 3, 0, 450, 80),
    ("АДК-2", "compressor", 2, 0, 580, 80),
    ("АДК-1", "compressor", 1, 0, 710, 80),
    ("ПС-3", "ps", 0, 2.3, 450, 190),
    ("ПС-2", "ps", 0, 2.1, 580, 190),
    ("ПС-1", "ps", 0, 2.4, 710, 190),
    ("ПС-4", "ps", 0, 2.0, 1150, 190),
    ("МО-3", "mo", 0, 0, 450, 430),
    ("МО-2", "mo", 0, 0, 580, 430),
    ("МО-1", "mo", 0, 0, 710, 430),
    ("АВО-5.5а", "avo", 25, 0, 360, 380),
    ("ГЛ-1", "gl", 0, 0, 490, 410),
    ("КТВ-1", "ktv", 0, 0, 450, 660),
    ("КТВ-2", "ktv", 0, 0, 580, 660),
    ("КТВ-3", "ktv", 0, 0, 710, 660),
    ("КТВ-4", "ktv", 0, 0, 840, 660),
    ("КТВ-5", "ktv", 0, 0, 970, 660),
    ("ДАО-550", "compressor", -32, 0, 950, 130),
    ("РЛ-1", "rl", -4, 0, 1150, 370),
    ("РЛ-2", "rl", -5, 0, 1150, 430),
    ("РЛ-3", "rl", -6, 0, 1150, 490),
    ("РЛ-4", "rl", -7, 0, 1050, 620),
]

for name, e_type, temp, press, x, y in elements:
    RefrigerationElement.objects.create(
        name=name,
        element_type=e_type,
        status='normal',
        temperature=temp,
        pressure=press,
        pos_x=x,
        pos_y=y,
    )

print(f"✅ Создано {len(elements)} элементов.")