from django import forms

class IngresoForm(forms.Form):
    nombre_persona = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'dark-input'}))
    # Campos adicionales se pueden agregar según la lógica real

    def save(self):
        # Placeholder: la implementación real debe crear Movimiento y DetalleMovimiento
        return None


class EgresoForm(forms.Form):
    nombre_persona = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class':'dark-input'}))
    cedula = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class':'dark-input'}))

    def save(self):
        # Placeholder: la implementación real debe crear Movimiento y DetalleMovimiento y ajustar stock
        return None
