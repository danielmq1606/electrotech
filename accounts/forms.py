"""
Formularios de la aplicación 'accounts'.
Inicio de sesión, creación de administradores y cambio de contraseñas.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario


class LoginForm(AuthenticationForm):
    """
    Formulario de inicio de sesión personalizado.
    Usa email como campo de identificación en lugar de username.
    """
    username = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'placeholder': 'correo@ejemplo.com',
            'autocomplete': 'email',
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
        })
    )
    
    error_messages = {
        'invalid_login': 'Correo electrónico o contraseña incorrectos. Verifique los datos.',
        'inactive': 'Esta cuenta está desactivada. Contacte al super administrador.',
    }


class CrearAdminForm(forms.ModelForm):
    """
    Formulario para que el super-admin cree cuentas de administrador.
    """
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
            'placeholder': 'Mínimo 8 caracteres',
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
            'placeholder': 'Repita la contraseña',
        })
    )
    
    class Meta:
        model = Usuario
        fields = ['email', 'username']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
                'placeholder': 'correo@ejemplo.com',
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
                'placeholder': 'Nombre de usuario',
            }),
        }
    
    def clean_email(self):
        """Valida que el correo no esté ya registrado."""
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario registrado con este correo electrónico.')
        return email
    
    def clean(self):
        """Valida que las contraseñas coincidan."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden. Intente de nuevo.')
        
        if password1 and len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        return cleaned_data
    
    def save(self, commit=True):
        """Crea el usuario administrador con la contraseña proporcionada."""
        usuario = super().save(commit=False)
        usuario.rol = Usuario.Rol.ADMIN
        usuario.set_password(self.cleaned_data['password1'])
        if commit:
            usuario.save()
        return usuario


class CambiarPasswordForm(forms.Form):
    """
    Formulario para que el super-admin cambie la contraseña de un administrador.
    """
    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(rol=Usuario.Rol.ADMIN, is_active=True),
        label='Administrador',
        empty_label='Seleccione un administrador...',
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
        })
    )
    nueva_password = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
            'placeholder': 'Mínimo 8 caracteres',
        })
    )
    confirmar_password = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border-2 border-gray-200 focus:border-electro-primary focus:ring-2 focus:ring-electro-primary/20 transition-all',
            'placeholder': 'Repita la contraseña',
        })
    )
    
    def clean(self):
        """Valida que las contraseñas coincidan y tengan longitud mínima."""
        cleaned_data = super().clean()
        nueva = cleaned_data.get('nueva_password')
        confirmar = cleaned_data.get('confirmar_password')
        
        if nueva and confirmar and nueva != confirmar:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        
        if nueva and len(nueva) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        return cleaned_data
