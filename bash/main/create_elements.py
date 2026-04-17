import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bash.settings')
django.setup()

from main.models import RefrigerationElement

def create_all_elements():
    RefrigerationElement.objects.all().delete()
    print("✓ Существующие данные очищены")
    
    elements = [
        # Кристаллизаторы (КР)
        {'name': 'КР-6', 'element_type': 'kp', 'status': 'normal', 'temperature': -17.7, 'ammonia_temp': -15.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 100},
        {'name': 'КР-7', 'element_type': 'kp', 'status': 'normal', 'temperature': -22.0, 'ammonia_temp': -19.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 170},
        {'name': 'КР-8', 'element_type': 'kp', 'status': 'normal', 'temperature': -20.6, 'ammonia_temp': -17.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 240},
        {'name': 'КР-9', 'element_type': 'kp', 'status': 'normal', 'temperature': -23.8, 'ammonia_temp': -21.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 310},
        {'name': 'КР-10', 'element_type': 'kp', 'status': 'normal', 'temperature': -19.2, 'ammonia_temp': -16.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 380},
        {'name': 'КР-10а', 'element_type': 'kp', 'status': 'normal', 'temperature': -20.5, 'ammonia_temp': -18.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 20, 'pos_y': 450},
        
        # Теплообменники (Т)
        {'name': 'Т-27', 'element_type': 't', 'status': 'normal', 'temperature': -11.7, 'ammonia_temp': -9.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 140, 'pos_y': 380},
        {'name': 'Т-27А', 'element_type': 't', 'status': 'normal', 'temperature': -12.9, 'ammonia_temp': -10.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 140, 'pos_y': 450},
        {'name': 'Т-27Б', 'element_type': 't', 'status': 'normal', 'temperature': -14.0, 'ammonia_temp': -11.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 140, 'pos_y': 520},
        {'name': 'Т-27В', 'element_type': 't', 'status': 'normal', 'temperature': -15.0, 'ammonia_temp': -12.0, 'pressure': 10.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 140, 'pos_y': 590},
        
        # Отделители жидкости (ОЖ)
        {'name': 'ОЖ-1', 'element_type': 'oz', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 8.0, 'level': 50, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 330, 'pos_y': 125},
        {'name': 'ОЖ-2', 'element_type': 'oz', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 8.0, 'level': 50, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 330, 'pos_y': 40},
        
        # Ресиверы дренажные (РД)
        {'name': 'РД-1', 'element_type': 'rd', 'status': 'normal', 'temperature': -10.0, 'ammonia_temp': -8.0, 'pressure': 12.0, 'level': 65.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 230, 'pos_y': 160},
        {'name': 'РД-2', 'element_type': 'rd', 'status': 'normal', 'temperature': -10.0, 'ammonia_temp': -8.0, 'pressure': 12.0, 'level': 45.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 300, 'pos_y': 160},
        
        # Компрессоры (АДК)
        {'name': 'АДК-1', 'element_type': 'compressor', 'status': 'normal', 'temperature': 25.0, 'ammonia_temp': 20.0, 'pressure': 15.0, 'level': 0, 'discharge_temp_stage1': 85.0, 'discharge_temp_stage2': 120.0, 'pos_x': 750, 'pos_y': 50},
        {'name': 'АДК-2', 'element_type': 'compressor', 'status': 'normal', 'temperature': 25.0, 'ammonia_temp': 20.0, 'pressure': 15.0, 'level': 0, 'discharge_temp_stage1': 82.0, 'discharge_temp_stage2': 118.0, 'pos_x': 590, 'pos_y': 50},
        {'name': 'АДК-3', 'element_type': 'compressor', 'status': 'normal', 'temperature': 25.0, 'ammonia_temp': 20.0, 'pressure': 15.0, 'level': 0, 'discharge_temp_stage1': 80.0, 'discharge_temp_stage2': 115.0, 'pos_x': 430, 'pos_y': 50},
        
        # ДАО
        {'name': 'ДАО-550', 'element_type': 'compressor', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 25.0, 'pressure': 18.0, 'level': 0, 'discharge_temp_stage1': 90.0, 'discharge_temp_stage2': 125.0, 'pos_x': 910, 'pos_y': 30},
        
        # Промышленные сосуды (ПС)
        {'name': 'ПС-1', 'element_type': 'ps', 'status': 'normal', 'temperature': -8.0, 'ammonia_temp': -6.0, 'pressure': 9.0, 'level': 55.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 770, 'pos_y': 220},
        {'name': 'ПС-2', 'element_type': 'ps', 'status': 'normal', 'temperature': -8.0, 'ammonia_temp': -6.0, 'pressure': 9.0, 'level': 48.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 610, 'pos_y': 220},
        {'name': 'ПС-3', 'element_type': 'ps', 'status': 'normal', 'temperature': -8.0, 'ammonia_temp': -6.0, 'pressure': 9.0, 'level': 52.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 450, 'pos_y': 220},
        {'name': 'ПС-4', 'element_type': 'ps', 'status': 'normal', 'temperature': -8.0, 'ammonia_temp': -6.0, 'pressure': 9.0, 'level': 60.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 1020, 'pos_y': 220},
        
        # Маслоотделители (МО)
        {'name': 'МО-1', 'element_type': 'mo', 'status': 'normal', 'temperature': 20.0, 'ammonia_temp': 18.0, 'pressure': 14.0, 'level': 30, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 720, 'pos_y': 360},
        {'name': 'МО-2', 'element_type': 'mo', 'status': 'normal', 'temperature': 20.0, 'ammonia_temp': 18.0, 'pressure': 14.0, 'level': 35, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 620, 'pos_y': 360},
        {'name': 'МО-3', 'element_type': 'mo', 'status': 'normal', 'temperature': 20.0, 'ammonia_temp': 18.0, 'pressure': 14.0, 'level': 28, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 520, 'pos_y': 360},
        
        # Маслосборник (МС)
        {'name': 'МС-1', 'element_type': 'ms', 'status': 'normal', 'temperature': 15.0, 'ammonia_temp': 12.0, 'pressure': 11.0, 'level': 40.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 820, 'pos_y': 360},
        
        # АВО
        {'name': 'АВО-5.5а', 'element_type': 'avo', 'status': 'normal', 'temperature': 35.0, 'ammonia_temp': 30.0, 'pressure': 20.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 280, 'pos_y': 400},
        
        # Гаситель пульсаций
        {'name': 'ГП-1', 'element_type': 'gl', 'status': 'normal', 'temperature': 10.0, 'ammonia_temp': 8.0, 'pressure': 13.0, 'level': 0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 370, 'pos_y': 405},
        
        # Конденсаторы (КТВ)
        {'name': 'КТВ-1', 'element_type': 'ktv', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 28.0, 'pressure': 16.0, 'level': 75.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 350, 'pos_y': 650},
        {'name': 'КТВ-2', 'element_type': 'ktv', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 28.0, 'pressure': 16.0, 'level': 80.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 470, 'pos_y': 650},
        {'name': 'КТВ-3', 'element_type': 'ktv', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 28.0, 'pressure': 16.0, 'level': 70.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 590, 'pos_y': 650},
        {'name': 'КТВ-4', 'element_type': 'ktv', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 28.0, 'pressure': 16.0, 'level': 65.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 710, 'pos_y': 650},
        {'name': 'КТВ-5', 'element_type': 'ktv', 'status': 'normal', 'temperature': 30.0, 'ammonia_temp': 28.0, 'pressure': 16.0, 'level': 72.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 830, 'pos_y': 650},
        
        # Ресиверы линейные (РЛ)
        {'name': 'РЛ-1', 'element_type': 'rl', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 10.0, 'level': 70.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 1100, 'pos_y': 380},
        {'name': 'РЛ-2', 'element_type': 'rl', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 10.0, 'level': 55.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 1100, 'pos_y': 470},
        {'name': 'РЛ-3', 'element_type': 'rl', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 10.0, 'level': 80.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 1100, 'pos_y': 560},
        {'name': 'РЛ-4', 'element_type': 'rl', 'status': 'normal', 'temperature': -5.0, 'ammonia_temp': -3.0, 'pressure': 10.0, 'level': 60.0, 'discharge_temp_stage1': 0, 'discharge_temp_stage2': 0, 'pos_x': 1050, 'pos_y': 730},
    ]
    
    for elem_data in elements:
        element = RefrigerationElement.objects.create(**elem_data)
        print(f"✓ Создан: {element.name}")
    
    print(f"\n✅ Всего создано: {RefrigerationElement.objects.count()} элементов")

if __name__ == '__main__':
    create_all_elements()