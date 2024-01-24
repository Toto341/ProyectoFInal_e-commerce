from django import forms
from .models import UserProfile, Productos, ProductosMarcas, ProductosCategorias

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']  

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Personalizar el campo 'categoria'
            self.fields['categoria'].widget = forms.Select(attrs={'class': 'form-control'})
            self.fields['categoria'].queryset = ProductosCategorias.objects.all()

            # Personalizar el campo 'marca'
            self.fields['marca'].widget = forms.Select(attrs={'class': 'form-control'})   
            self.fields['marca'].queryset = ProductosMarcas.objects.all() 

            # Ocultar el campo 'id_usuario' y asignar el usuario actual automáticamente
            self.fields['id_usuario'].widget = forms.HiddenInput()
            self.fields['id_usuario'].required = False

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.id_usuario = self.instance.id_usuario if self.instance else self.initial['id_usuario']
        if commit:
            instance.save()
        return instance            



class ContactoForm(forms.Form):
     nombre = forms.CharField(label='Nombre', max_length=100)
     email  = forms.EmailField(label='Email')
     mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)