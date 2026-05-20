"""
Rutas de la aplicación 'movements'.
Gestión de ingresos, egresos y generación de planillas PDF.
"""

from django.urls import path
from . import views

app_name = 'movements'

urlpatterns = [
    # Ingreso de componentes
    path('ingreso/', views.ingreso_componentes, name='ingreso'),
    path('ingreso/planilla/<int:pk>/', views.planilla_ingreso, name='planilla_ingreso'),
    path('ingreso/pdf/<int:pk>/', views.pdf_ingreso, name='pdf_ingreso'),
    
    # Egreso de componentes
    path('egreso/', views.egreso_componentes, name='egreso'),
    path('egreso/planilla/<int:pk>/', views.planilla_egreso, name='planilla_egreso'),
    path('egreso/pdf/<int:pk>/', views.pdf_egreso, name='pdf_egreso'),
    
    # Buscar componente por nombre (para autocompletar en formularios)
    path('api/buscar-componente/', views.buscar_componente, name='buscar_componente'),
]
