from django.urls import path
from django.views.generic import TemplateView
from .views import pagina_principal

app_name = 'scrum'

urlpatterns = [
    path('',pagina_principal,name="pagina_principal")
]
