from django.db.models import fields
from django import forms
from django.forms import widgets
from .models import *
from django.forms import DateTimeInput

class DateInput(forms.DateInput):
    input_type = 'date'

class LocalidadForm(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

class ObraSocialForm(forms.ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'direccion':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'disponible':forms.CheckboxInput(attrs={
                'class':'form-check-input'
            })
        }

    


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
        'fecha_nac': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
                }),
        }
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets ={
            'persona': forms.Select(attrs={
                'name':'persona',
                'id':'persona'
            })
        }

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional 
        fields = '__all__'
        widgets ={
            'persona': forms.Select(attrs={
                'name':'persona',
                'id':'persona'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ProfesionalForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'

        widgets ={
                'localidad': forms.Select(attrs={
                    'readonly':'readonly'
                })
            }

    def __init__(self, *args, **kwargs):
        super(EstablecimientoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   

class TurnoForm(forms.ModelForm):
    
    fecha = forms.DateTimeField(
            input_formats = ['%Y-%m-%dT%H:%M'],
            widget = forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control'},
                format='%Y-%m-%dT%H:%M')
        )
    class Meta:
        model = Turno
        fields = '__all__'
        widget = {
            'paciente': forms.Select(attrs={
                'name':'paciente',
                'id':'paciente'
            })
        }
        
    
    def __init__(self, *args, **kwargs):
        super(TurnoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'   