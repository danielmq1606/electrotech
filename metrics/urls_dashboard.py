"""
Rutas específicas para el dashboard (raíz de la app).
Separadas de las rutas de métricas para mantener limpieza.
"""

from django.urls import path
from metrics import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='inicio'),
]
