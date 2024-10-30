from django import forms
from .models import Epica, User, Sprint, Tarea

class EpicaForm(forms.ModelForm):
    class Meta:
        model = Epica
        fields = ['nombre', 'descripcion', 'criterios_aceptacion', 'estado',
                   'esfuerzo_estimado_total', 'fecha_inicio','fecha_fin', 'progreso',
                   'responsable_id']

class SprintForm(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = ['nombre','objetivo','fecha_inicio','fecha_fin','velocidad',
                  'fecha_creacion','fecha_actualizacion','scrum_master_id']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','criterios_aceptacion','prioridad',
                  'estado','esfuerzo_estimado','fecha_de_creacion','fecha_de_actualizacion',
                  'bloqueadores','responsable_id','sprint_asignado_id']