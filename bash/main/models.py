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
        ('valve', 'Клапан'),
    ]
    
    STATUS_CHOICES = [
        ('normal', 'Норма'),
        ('warning', 'Предупреждение'),
        ('alarm', 'Авария'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название")
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