from django.contrib import admin
from .models import Epica, Tarea, Sprint

@admin.register(Epica)
class EpicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'criterios_aceptacion', 'estado',
                   'esfuerzo_estimado_total', 'fecha_inicio','fecha_fin', 'progreso',
                   'responsable_id']
    
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo','descripcion','criterios_aceptacion','prioridad',
                  'estado','esfuerzo_estimado','responsable','sprint_asignado',
                  'fecha_de_creacion','fecha_de_actualizacion','bloqueadores',
                  'responsable_id','sprint_asignado_id']
    
    
@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['nombre','objetivo','fecha_inicio','fecha_fin','velocidad',
                  'scrum_master','fecha_creacion','fecha_actualizacion','scrum_master_id']
