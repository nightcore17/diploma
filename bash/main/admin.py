from django.contrib import admin
from .models import RefrigerationElement, Brigade, WeatherForecast

@admin.register(RefrigerationElement)
class RefrigerationElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'element_type', 'status', 'temperature', 'pressure', 'level')
    list_filter = ('element_type', 'status')
    search_fields = ('name',)
    list_editable = ('status', 'temperature', 'pressure', 'level')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'element_type', 'status')
        }),
        ('Общие параметры', {
            'fields': ('temperature', 'ammonia_temp', 'pressure', 'level')
        }),
        ('Параметры компрессоров', {
            'fields': ('discharge_temp_stage1', 'discharge_temp_stage2'),
            'classes': ('collapse',)
        }),
        ('Позиция на схеме', {
            'fields': ('pos_x', 'pos_y')
        }),
    )
    
    actions = ['stop_selected', 'start_selected']
    
    def stop_selected(self, request, queryset):
        queryset.update(status='stopped')
        self.message_user(request, f'⏹️ Остановлено элементов: {queryset.count()}')
    stop_selected.short_description = "⏹️ Остановить выбранные аппараты"
    
    def start_selected(self, request, queryset):
        queryset.update(status='normal')
        self.message_user(request, f'▶️ Запущено элементов: {queryset.count()}')
    start_selected.short_description = "▶️ Запустить выбранные аппараты"

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'is_working')
    list_editable = ('is_working',)

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature_day', 'temperature_night', 'condition', 'humidity', 'wind_speed')
    list_filter = ('condition',)