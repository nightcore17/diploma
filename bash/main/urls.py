from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('full-schema/', views.full_schema, name='full_schema'),
    path('full_schema/', views.full_schema),  # запасной вариант
    path('element/<int:element_id>/', views.element_detail, name='element_detail'),
    path('weather/', views.weather_forecast, name='weather'),
    path('api/update-element/', views.update_element, name='update_element'),
    path('api/get-data/', views.get_data, name='get_data'),
    path('api/update-weather/', views.update_weather, name='update_weather'),
]