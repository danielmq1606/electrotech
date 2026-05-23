"""
Vistas de la aplicación 'movements'.
Formularios de ingreso y egreso, generación de planillas PDF.
Implementación mínima con CBV para ingreso y egreso (CreateView).
"""

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import IngresoForm, EgresoForm


@method_decorator(login_required, name='dispatch')
class IngresoCreateView(FormView):
    """Vista para registrar ingresos de componentes (FormView para forms.Form)."""
    form_class = IngresoForm
    template_name = 'movements/ingreso.html'
    success_url = reverse_lazy('movements:ingreso')

    def form_valid(self, form):
        # Guardar movimiento con el usuario actual
        try:
            movimiento = form.save(user=self.request.user)
        except Exception as e:
            # Si la forma lanza ValidationError, agregar los errores al formulario
            from django.core.exceptions import ValidationError
            if isinstance(e, ValidationError):
                if hasattr(e, 'message_dict'):
                    for f, msgs in e.message_dict.items():
                        for m in msgs:
                            form.add_error(f, m)
                else:
                    form.add_error(None, e.message)
            else:
                form.add_error(None, str(e))
            return self.form_invalid(form)

        messages.success(self.request, 'Ingreso registrado correctamente.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EgresoCreateView(FormView):
    """Vista para registrar egresos de componentes (FormView para forms.Form)."""
    form_class = EgresoForm
    template_name = 'movements/egreso.html'
    success_url = reverse_lazy('movements:egreso')

    def form_valid(self, form):
        try:
            movimiento = form.save(user=self.request.user)
        except Exception as e:
            from django.core.exceptions import ValidationError
            if isinstance(e, ValidationError):
                if hasattr(e, 'message_dict'):
                    for f, msgs in e.message_dict.items():
                        for m in msgs:
                            form.add_error(f, m)
                else:
                    form.add_error(None, e.message)
            else:
                form.add_error(None, str(e))
            return self.form_invalid(form)

        messages.success(self.request, 'Egreso registrado correctamente.')
        return super().form_valid(form)


# Mantener vistas auxiliares (planilla/pdf) como placeholders

def planilla_ingreso(request, pk):
    """Vista previa de planilla de ingreso para impresión."""
    return render(request, 'movements/planilla_ingreso.html')


def pdf_ingreso(request, pk):
    """Genera y descarga el PDF de una planilla de ingreso."""
    # Implementar generación ReportLab más adelante
    pass


def planilla_egreso(request, pk):
    """Vista previa de planilla de egreso para impresión."""
    return render(request, 'movements/planilla_egreso.html')


def pdf_egreso(request, pk):
    """Genera y descarga el PDF de una planilla de egreso."""
    # Implementar generación ReportLab más adelante
    pass


def buscar_componente(request):
    """API: busca componentes por nombre para autocompletar."""
    # Implementación pendiente (devolver JSON)
    pass


# Function wrappers for compatibility with existing urls.py
def ingreso_componentes(request):
    """Compatibilidad: interfaz basada en funciones para ingreso."""
    view = IngresoCreateView.as_view()
    return view(request)


def egreso_componentes(request):
    """Compatibilidad: interfaz basada en funciones para egreso."""
    view = EgresoCreateView.as_view()
    return view(request)
