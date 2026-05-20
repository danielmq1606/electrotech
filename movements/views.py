"""
Vistas de la aplicación 'movements'.
Formularios de ingreso y egreso, generación de planillas PDF.
"""

from django.shortcuts import render


def ingreso_componentes(request):
    """Formulario para registrar ingreso de componentes."""
    return render(request, 'movements/ingreso.html')


def planilla_ingreso(request, pk):
    """Vista previa de planilla de ingreso para impresión."""
    return render(request, 'movements/planilla_ingreso.html')


def pdf_ingreso(request, pk):
    """Genera y descarga el PDF de una planilla de ingreso."""
    pass


def egreso_componentes(request):
    """Formulario para registrar egreso de componentes."""
    return render(request, 'movements/egreso.html')


def planilla_egreso(request, pk):
    """Vista previa de planilla de egreso para impresión."""
    return render(request, 'movements/planilla_egreso.html')


def pdf_egreso(request, pk):
    """Genera y descarga el PDF de una planilla de egreso."""
    pass


def buscar_componente(request):
    """API: busca componentes por nombre para autocompletar."""
    pass
