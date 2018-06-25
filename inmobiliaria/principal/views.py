from django.shortcuts import render

# Create your views here.

from principal.models import inmueble

def lista_inmuebles(request):
    inmuebles = inmueble.objects.all()
    return render(request, 'listado.html', {'lista': inmuebles})
