from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import (
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)

# Create your views here.

@login_required
def pagina_principal(request):
    return HttpResponse("PAGINA PRINCIPAL")