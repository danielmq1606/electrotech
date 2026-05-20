"""
Rutas de la aplicación 'metrics'.
Dashboard principal, métricas con gráficas e historial de movimientos.
"""

from django.urls import path
from . import views

app_name = 'metrics'

urlpatterns = [
    # Dashboard principal
    path('', views.dashboard, name='dashboard'),
    
    # Métricas con gráficas
    path('graficas/', views.metricas_graficas, name='graficas'),
    
    # API para datos de gráficas (JSON para Chart.js)
    path('api/datos-grafica/', views.api_datos_grafica, name='api_datos_grafica'),
    
    # Historial de movimientos
    path('historial/', views.historial, name='historial'),
    path('historial/planilla/<int:pk>/', views.ver_planilla_historica, name='ver_planilla'),
]
