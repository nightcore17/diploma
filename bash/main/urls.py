from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('full-schema/', views.full_schema, name='full_schema'),  # ЭТУ СТРОКУ ДОБАВЬ
    path('element/<int:element_id>/', views.element_detail, name='element_detail'),
    path('api/update-element/', views.update_element, name='update_element'),
    path('api/get-data/', views.get_data, name='get_data'),
]