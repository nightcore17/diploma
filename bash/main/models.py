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
    
    temperature = models.FloatField(default=0, verbose_name="Температура сырья")
    ammonia_temp = models.FloatField(default=0, verbose_name="Температура аммиака")
    pressure = models.FloatField(default=0, verbose_name="Давление")
    level = models.FloatField(default=50, verbose_name="Уровень (%)")
    
    discharge_temp_stage1 = models.FloatField(default=0, verbose_name="Температура нагнетания 1 ступени")
    discharge_temp_stage2 = models.FloatField(default=0, verbose_name="Температура нагнетания 2 ступени")
    
    pos_x = models.IntegerField(default=0)
    pos_y = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} ({self.get_element_type_display()})"
    
    def stop_element(self):
        self.status = 'stopped'
        self.save()
    
    def start_element(self):
        self.status = 'normal'
        self.save()

class WeatherForecast(models.Model):
    date = models.DateField(verbose_name="Дата")
    temperature_day = models.IntegerField(verbose_name="Температура днём (°C)")
    temperature_night = models.IntegerField(verbose_name="Температура ночью (°C)")
    condition = models.CharField(max_length=50, default="Ясно", verbose_name="Состояние")
    humidity = models.IntegerField(default=70, verbose_name="Влажность (%)")
    wind_speed = models.IntegerField(default=3, verbose_name="Ветер (м/с)")
    icon = models.CharField(max_length=20, default="☀️", verbose_name="Иконка")
    
    class Meta:
        verbose_name = "Прогноз погоды"
        verbose_name_plural = "Прогнозы погоды"
        ordering = ['date']
    
    def __str__(self):
        return f"{self.date} - {self.condition}"

class RawMaterial(models.Model):
    MATERIAL_TYPES = [
        ('oil_3', 'Масло 3 фракция'),
        ('oil_4', 'Масло 4 фракция'),
        ('oil_5', 'Масло 5 фракция'),
        ('paraffin', 'Парафин'),
        ('zvp', 'ЗВП (Застывающие вещества)'),
    ]
    
    name = models.CharField(max_length=100, choices=MATERIAL_TYPES, unique=True, verbose_name="Тип сырья")
    total_volume = models.FloatField(default=0, verbose_name="Общий объём (м³)")
    current_volume = models.FloatField(default=0, verbose_name="Текущий остаток (м³)")
    temperature_required = models.FloatField(default=-20, verbose_name="Требуемая температура (°C)")
    freezing_point = models.FloatField(default=-10, verbose_name="Температура застывания (°C)")
    
    class Meta:
        verbose_name = "Тип сырья"
        verbose_name_plural = "Типы сырья"
    
    def __str__(self):
        return self.get_name_display()

class RawMaterialLoad(models.Model):
    STATUS_CHOICES = [
        ('planned', '📋 Запланирована'),
        ('in_progress', '🔄 В процессе'),
        ('completed', '✅ Завершена'),
        ('cancelled', '❌ Отменена'),
    ]
    
    material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE, verbose_name="Тип сырья")
    volume = models.FloatField(verbose_name="Объём (м³)")
    start_time = models.DateTimeField(verbose_name="Время начала", null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="Время окончания", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned', verbose_name="Статус")
    operator = models.CharField(max_length=100, default="", blank=True, verbose_name="Оператор")
    note = models.TextField(max_length=500, default="", blank=True, verbose_name="Примечание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    
    class Meta:
        verbose_name = "Загрузка сырья"
        verbose_name_plural = "Загрузки сырья"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.material} — {self.volume} м³ ({self.get_status_display()})"

class ShiftLog(models.Model):
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, verbose_name="Бригада")
    date = models.DateField(verbose_name="Дата")
    time_from = models.TimeField(verbose_name="Время с")
    time_to = models.TimeField(verbose_name="Время по")
    description = models.TextField(verbose_name="Описание работ")
    performed_by = models.CharField(max_length=100, verbose_name="Исполнитель")
    notes = models.TextField(default="", blank=True, verbose_name="Заметки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    
    class Meta:
        verbose_name = "Запись вахтового журнала"
        verbose_name_plural = "Вахтовый журнал"
        ordering = ['-date', '-time_from']
    
    def __str__(self):
        return f"{self.date} {self.time_from}-{self.time_to}: {self.description[:50]}"

class Order(models.Model):
    ORDER_FROM_CHOICES = [
        ('chief', 'Начальник установки'),
        ('deputy', 'Зам. начальника'),
        ('mechanic', 'Механик установки'),
    ]
    
    ORDER_STATUS_CHOICES = [
        ('active', '📋 Действующее'),
        ('in_progress', '🔄 Выполняется'),
        ('completed', '✅ Выполнено'),
        ('cancelled', '❌ Отменено'),
    ]
    
    order_from = models.CharField(max_length=20, choices=ORDER_FROM_CHOICES, verbose_name="От кого")
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, verbose_name="Бригада")
    description = models.TextField(verbose_name="Содержание распоряжения")
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='active', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    deadline = models.DateTimeField(null=True, blank=True, verbose_name="Срок выполнения")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Выполнено")
    
    class Meta:
        verbose_name = "Распоряжение"
        verbose_name_plural = "Распоряжения"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_order_from_display()}: {self.description[:60]}"