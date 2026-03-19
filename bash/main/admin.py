from django.contrib import admin
from .models import RefrigerationElement, Brigade, WeatherForecast

@admin.register(RefrigerationElement)
class RefrigerationElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'element_type', 'status', 'temperature', 'pressure', 'pos_x', 'pos_y')
    list_editable = ('temperature', 'pressure', 'status', 'pos_x', 'pos_y')
    list_filter = ('element_type', 'status')
    search_fields = ('name',)

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'is_working')

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature_day', 'condition', 'icon')