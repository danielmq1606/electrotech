from django import forms
from django.core.exceptions import ValidationError

from inventory.models import Componente
from .models import Movimiento, DetalleMovimiento


class BaseMovimientoForm(forms.Form):
    componente = forms.ModelChoiceField(
        queryset=Componente.objects.all(),
        label='Componente',
        widget=forms.Select(attrs={'class': 'dark-select'})
    )
    cantidad = forms.IntegerField(
        min_value=1,
        label='Cantidad',
        widget=forms.NumberInput(attrs={'class': 'dark-input', 'min': 1})
    )
    nombre_persona = forms.CharField(
        label='Nombre de la persona',
        widget=forms.TextInput(attrs={'class': 'dark-input'})
    )
    cedula = forms.CharField(
        label='Cédula / ID',
        required=False,
        widget=forms.TextInput(attrs={'class': 'dark-input'})
    )
    cargo = forms.CharField(
        label='Cargo',
        required=False,
        widget=forms.TextInput(attrs={'class': 'dark-input'})
    )
    departamento = forms.CharField(
        label='Departamento',
        required=False,
        widget=forms.TextInput(attrs={'class': 'dark-input'})
    )


class IngresoForm(BaseMovimientoForm):
    """Formulario para registrar ingresos.

    El método save(user) crea Movimiento y DetalleMovimiento, actualiza el stock
    del componente y devuelve la instancia de Movimiento creada.
    """

    def save(self, user):
        data = self.cleaned_data
        componente = data['componente']
        cantidad = data['cantidad']

        # Crear movimiento
        movimiento = Movimiento.objects.create(
            tipo=Movimiento.Tipo.INGRESO,
            numero_planilla='',
            usuario=user,
            nombre_persona=data.get('nombre_persona', ''),
            cedula=data.get('cedula', ''),
            cargo=data.get('cargo', ''),
            departamento=data.get('departamento', ''),
        )
        # Generar número de planilla (usa pk)
        movimiento.generar_numero_planilla()

        # Crear detalle y snapshot
        detalle = DetalleMovimiento(
            movimiento=movimiento,
            componente=componente,
            cantidad=cantidad,
        )
        detalle.guardar_snapshot()
        detalle.save()

        # Actualizar stock (campo 'cantidad' en Componente)
        componente.cantidad = (componente.cantidad or 0) + cantidad
        componente.save(update_fields=['cantidad'])

        return movimiento


class EgresoForm(BaseMovimientoForm):
    motivo = forms.CharField(
        label='Motivo',
        required=False,
        widget=forms.Textarea(attrs={'class': 'dark-textarea'})
    )

    def clean(self):
        cleaned = super().clean()
        componente = cleaned.get('componente')
        cantidad = cleaned.get('cantidad')
        if componente and cantidad is not None:
            if cantidad > (componente.cantidad or 0):
                raise ValidationError({'cantidad': 'La cantidad solicitada excede el stock disponible.'})
        return cleaned

    def save(self, user):
        data = self.cleaned_data
        componente = data['componente']
        cantidad = data['cantidad']

        # Crear movimiento de egreso
        movimiento = Movimiento.objects.create(
            tipo=Movimiento.Tipo.EGRESO,
            numero_planilla='',
            usuario=user,
            nombre_persona=data.get('nombre_persona', ''),
            cedula=data.get('cedula', ''),
            cargo=data.get('cargo', ''),
            departamento=data.get('departamento', ''),
        )
        movimiento.generar_numero_planilla()

        # Crear detalle y snapshot
        detalle = DetalleMovimiento(
            movimiento=movimiento,
            componente=componente,
            cantidad=cantidad,
        )
        detalle.guardar_snapshot()
        detalle.save()

        # Restar del stock
        componente.cantidad = (componente.cantidad or 0) - cantidad
        if componente.cantidad < 0:
            componente.cantidad = 0
        componente.save(update_fields=['cantidad'])

        return movimiento
