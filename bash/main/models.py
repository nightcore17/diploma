from django.db import models

class Brigade(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    leader = models.CharField(max_length=100, verbose_name="Бригадир")
    is_working = models.BooleanField(default=True, verbose_name="Работает")
    
    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"
    
    def __str__(self):
        return self.name

class RefrigerationElement(models.Model):
    ELEMENT_TYPES = [
        ('compressor', 'Компрессор'),
        ('evaporator', 'Испаритель'),
        ('condenser', 'Конденсатор'),
        ('sensor', 'Датчик'),
        ('vessel', 'Сосуд'),
        ('separator', 'Сепаратор'),
        ('receiver', 'Ресивер'),
        ('heat_exchanger', 'Теплообменник'),
        ('filter', 'Фильтр'),
        ('damper', 'Гаситель пульсаций'),
        ('oil_separator', 'Маслоотделитель'),
    ]
    
    STATUS_CHOICES = [
        ('normal', 'Норма'),
        ('warning', 'Предупреждение'),
        ('alarm', 'Авария'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название (например КР-6)")
    element_type = models.CharField(max_length=20, choices=ELEMENT_TYPES, default='sensor', verbose_name="Тип")
    temperature = models.FloatField(default=0, verbose_name="Температура")
    pressure = models.FloatField(default=0, verbose_name="Давление")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='normal', verbose_name="Статус")
    pos_x = models.IntegerField(default=100, verbose_name="Позиция X")
    pos_y = models.IntegerField(default=100, verbose_name="Позиция Y")
    
    class Meta:
        verbose_name = "Элемент"
        verbose_name_plural = "Элементы"
    
    def __str__(self):
        return self.name

    @property
    def template_name(self):
        """Превращает КР-6 в КР_6 для шаблона"""
        return self.name.replace('-', '_').replace('.', '_').replace(' ', '_')

class WeatherForecast(models.Model):
    date = models.DateField(verbose_name="Дата")
    temperature_day = models.IntegerField(verbose_name="Температура днем")
    temperature_night = models.IntegerField(verbose_name="Температура ночью")
    condition = models.CharField(max_length=50, verbose_name="Погода", default="Ясно")
    humidity = models.IntegerField(default=70, verbose_name="Влажность")
    wind_speed = models.IntegerField(default=3, verbose_name="Ветер, м/с")
    icon = models.CharField(max_length=20, default="☀️")
    
    class Meta:
        ordering = ['date']
        verbose_name = "Прогноз погоды"
        verbose_name_plural = "Прогнозы погоды"
    
    def __str__(self):
        return f"{self.date}: {self.temperature_day}°C"