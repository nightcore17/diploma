from django.db import models

class Brigade(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    leader = models.CharField(max_length=100, verbose_name="Бригадир")
    is_working = models.BooleanField(default=True, verbose_name="Работает")
    
    def __str__(self):
        return self.name

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

    def __str__(self):
        return f"{self.date}: {self.temperature_day}°C"

class RefrigerationElement(models.Model):
    ELEMENT_TYPES = [
        ('kp', 'Кристаллизатор'),
        ('compressor', 'Компрессор'),
        ('rd', 'Ресивер дренажный'),
        ('oz', 'Отделитель жидкости'),
        ('t', 'Теплообменник'),
        ('ps', 'Промышленный сосуд'),
        ('mo', 'Маслоотделитель'),
        ('avo', 'Аппарат воздушного охлаждения'),
        ('gl', 'Гаситель пульсаций'),
        ('ktv', 'Конденсатор'),
        ('rl', 'Ресивер линейный'),
    ]
    
    STATUS_CHOICES = [
        ('normal', 'Норма'),
        ('warning', 'Предупреждение'),
        ('alarm', 'Авария'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название")
    element_type = models.CharField(max_length=20, choices=ELEMENT_TYPES, default='kp', verbose_name="Тип")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='normal', verbose_name="Статус")
    temperature = models.FloatField(default=0, verbose_name="Температура (°C)")
    pressure = models.FloatField(default=0, verbose_name="Давление (бар)")
    pos_x = models.IntegerField(default=0, verbose_name="Координата X")
    pos_y = models.IntegerField(default=0, verbose_name="Координата Y")
    
    class Meta:
        verbose_name = "Элемент схемы"
        verbose_name_plural = "Элементы схемы"
    
    def __str__(self):
        return self.name