from django.db import models

class Brigade(models.Model):
    name = models.CharField(max_length=100)
    leader = models.CharField(max_length=100)
    is_working = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class RefrigerationElement(models.Model):
    ELEMENT_TYPES = [
        ('kp', 'Кристаллизатор'),
        ('t', 'Теплообменник'),
        ('compressor', 'Компрессор'),
        ('rd', 'Ресивер дренажный'),
        ('oz', 'Отделитель жидкости'),
        ('ps', 'Промышленный сосуд'),
        ('mo', 'Маслоотделитель'),
        ('avo', 'АВО'),
        ('gl', 'Гаситель пульсаций'),
        ('ktv', 'Конденсатор'),
        ('rl', 'Ресивер линейный'),
        ('ms', 'Маслосборник'),
    ]
    
    STATUS_CHOICES = [
        ('normal', '✅ В работе'),
        ('warning', '⚠️ Внимание'),
        ('alarm', '🔴 Авария'),
        ('stopped', '⏹️ Остановлен'),
    ]
    
    name = models.CharField(max_length=100)
    element_type = models.CharField(max_length=20, choices=ELEMENT_TYPES, default='kp')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='normal')
    
    # Общие параметры
    temperature = models.FloatField(default=0, verbose_name="Температура сырья")
    ammonia_temp = models.FloatField(default=0, verbose_name="Температура аммиака")
    pressure = models.FloatField(default=0, verbose_name="Давление")
    level = models.FloatField(default=50, verbose_name="Уровень (%)")
    
    # Специфические параметры для компрессоров
    discharge_temp_stage1 = models.FloatField(default=0, verbose_name="Температура нагнетания 1 ступени")
    discharge_temp_stage2 = models.FloatField(default=0, verbose_name="Температура нагнетания 2 ступени")
    
    # Позиция на схеме
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.get_element_type_display()})"
    
    def stop_element(self):
        """Остановка аппарата"""
        self.status = 'stopped'
        self.save()
    
    def start_element(self):
        """Запуск аппарата"""
        self.status = 'normal'
        self.save()

class WeatherForecast(models.Model):
    date = models.DateField()
    temperature_day = models.IntegerField()
    temperature_night = models.IntegerField()
    condition = models.CharField(max_length=50, default="Ясно")
    humidity = models.IntegerField(default=70)
    wind_speed = models.IntegerField(default=3)
    icon = models.CharField(max_length=20, default="☀️")
    
    def __str__(self):
        return f"{self.date} - {self.condition}"