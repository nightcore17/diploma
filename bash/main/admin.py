from django.contrib import admin
from .models import Brigade, RefrigerationElement

@admin.register(Brigade)
class BrigadeAdmin(admin.ModelAdmin):
    list_display = ['name', 'leader', 'is_working']

@admin.register(RefrigerationElement)
class RefrigerationElementAdmin(admin.ModelAdmin):
    list_display = ['name', 'temperature', 'pressure', 'status', 'pos_x', 'pos_y']
    list_editable = ['temperature', 'pressure', 'status']