from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('element/<int:element_id>/', views.element_detail, name='element_detail'),
    path('element/<int:element_id>/data/', views.element_data, name='element_data'),
    path('full-schema/', views.full_schema, name='full_schema'),
    path('weather/', views.weather_forecast, name='weather'),
    path('api/update-element/', views.update_element, name='update_element'),
    path('api/update-level/', views.update_level, name='update_level'),
    path('api/toggle-status/', views.toggle_status, name='toggle_status'),
    path('api/random-update/', views.random_update, name='random_update'),
    path('api/get-data/', views.get_data, name='get_data'),
    path('api/update-weather/', views.update_weather, name='update_weather'),
]