from django.contrib import admin
from django.utils import timezone
from .models import (
    RefrigerationElement, Brigade, WeatherForecast, 
    RawMaterial, RawMaterialLoad, ShiftLog, Order
)

@admin.register(RefrigerationElement)
class RefrigerationElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'element_type', 'status', 'temperature', 'pressure', 'level')
    list_filter = ('element_type', 'status')
    search_fields = ('name',)
    list_editable = ('status', 'temperature', 'pressure', 'level')
    
    fieldsets = (
        ('Основная информация', {'fields': ('name', 'element_type', 'status')}),
        ('Общие параметры', {'fields': ('temperature', 'ammonia_temp', 'pressure', 'level')}),
        ('Параметры компрессоров', {'fields': ('discharge_temp_stage1', 'discharge_temp_stage2'), 'classes': ('collapse',)}),
        ('Позиция на схеме', {'fields': ('pos_x', 'pos_y')}),
    )
    
    actions = ['stop_selected', 'start_selected']
    
    def stop_selected(self, request, queryset):
        queryset.update(status='stopped')
        self.message_user(request, f'⏹️ Остановлено: {queryset.count()}')
    stop_selected.short_description = "⏹️ Остановить"
    
    def start_selected(self, request, queryset):
        queryset.update(status='normal')
        self.message_user(request, f'▶️ Запущено: {queryset.count()}')
    start_selected.short_description = "▶️ Запустить"

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'is_working')
    list_editable = ('is_working',)

@admin.register(WeatherForecast)
class WeatherForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature_day', 'temperature_night', 'condition', 'humidity', 'wind_speed', 'icon')
    list_filter = ('condition', 'date')
    list_editable = ('temperature_day', 'temperature_night', 'condition', 'humidity', 'wind_speed', 'icon')
    ordering = ('date',)
    date_hierarchy = 'date'

@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ('get_name_display', 'total_volume', 'current_volume', 'temperature_required', 'freezing_point')
    list_editable = ('total_volume', 'current_volume', 'temperature_required', 'freezing_point')

@admin.register(RawMaterialLoad)
class RawMaterialLoadAdmin(admin.ModelAdmin):
    list_display = ('material', 'volume', 'status', 'operator', 'created_at')
    list_filter = ('status', 'material')
    list_editable = ('status', 'volume', 'operator')
    date_hierarchy = 'created_at'
    
    actions = ['mark_in_progress', 'mark_completed']
    
    def mark_in_progress(self, request, queryset):
        queryset.update(status='in_progress', start_time=timezone.now())
        self.message_user(request, f'🔄 В процессе: {queryset.count()}')
    mark_in_progress.short_description = "🔄 В процессе"
    
    def mark_completed(self, request, queryset):
        queryset.update(status='completed', end_time=timezone.now())
        self.message_user(request, f'✅ Завершено: {queryset.count()}')
    mark_completed.short_description = "✅ Завершить"

@admin.register(ShiftLog)
class ShiftLogAdmin(admin.ModelAdmin):
    list_display = ('date', 'time_from', 'time_to', 'description', 'performed_by', 'brigade')
    list_filter = ('date', 'brigade')
    search_fields = ('description', 'performed_by')
    date_hierarchy = 'date'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_order_from_display', 'description', 'brigade', 'status', 'created_at')
    list_filter = ('order_from', 'status', 'brigade')
    search_fields = ('description',)
    list_editable = ('status',)
    date_hierarchy = 'created_at'
    
    actions = ['mark_completed']
    
    def get_order_from_display(self, obj):
        return obj.get_order_from_display()
    get_order_from_display.short_description = 'От кого'
    
    def mark_completed(self, request, queryset):
        queryset.update(status='completed', completed_at=timezone.now())
        self.message_user(request, f'✅ Выполнено: {queryset.count()}')
    mark_completed.short_description = "✅ Отметить выполненным"