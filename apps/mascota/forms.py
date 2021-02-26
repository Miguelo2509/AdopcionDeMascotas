from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
			'nombre',
			'especie',
			'raza',
			'sexo',
			'fechaNac',
			'usuario',
			'vacuna',
		]
        labels = {
			'nombre': 'Nombre',
			'especie': 'Especie',
			'raza': 'Raza',
			'sexo': 'Sexo',
			'fechaNac': 'Fecha Nacimiento',
			'usuario': 'Usuario',
			'vacuna': 'Vacuna',
		}
        widgets	= {
			'nombre': forms.TextInput(attrs={'class':'form_control'}),
			'especie': forms.TextInput(attrs={'class':'form_control'}),
			'raza': forms.TextInput(attrs={'class':'form_control'}),
			'sexo': forms.TextInput(attrs={'class':'form_control'}),
			'fechaNac': forms.TextInput(attrs={'class':'form_control'}),
			'usuario': forms.Select(attrs={'class':'form_control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}	 
