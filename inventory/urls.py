"""
Rutas de la aplicación 'inventory'.
Gestión de categorías y componentes del inventario.
"""

from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # Listado de inventario tipo catálogo
    path('', views.listado_inventario, name='listado'),
    
    # Detalle de un componente
    path('componente/<int:pk>/', views.detalle_componente, name='detalle'),
    
    # CRUD de componentes
    path('componente/crear/', views.crear_componente, name='crear'),
    path('componente/<int:pk>/editar/', views.editar_componente, name='editar'),
    path('componente/<int:pk>/eliminar/', views.eliminar_componente, name='eliminar'),
    
    # Gestión de categorías (crear nueva desde formulario)
    path('categorias/', views.gestionar_categorias, name='categorias'),
]
