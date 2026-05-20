"""
Vistas de la aplicación 'inventory'.
Catálogo de inventario, detalle de componentes y operaciones CRUD.
"""

from django.shortcuts import render


def listado_inventario(request):
    """Vista principal del inventario tipo catálogo."""
    return render(request, 'inventory/listado.html')


def detalle_componente(request, pk):
    """Vista de detalle de un componente específico."""
    return render(request, 'inventory/detalle.html')


def crear_componente(request):
    """Formulario para crear un nuevo componente."""
    return render(request, 'inventory/crear.html')


def editar_componente(request, pk):
    """Formulario para editar un componente existente."""
    return render(request, 'inventory/editar.html')


def eliminar_componente(request, pk):
    """Confirma y elimina un componente."""
    return render(request, 'inventory/eliminar.html')


def gestionar_categorias(request):
    """Gestión de categorías (crear nuevas)."""
    return render(request, 'inventory/categorias.html')
