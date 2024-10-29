from django.shortcuts import render
from .models import Catalogo
# Create your views here.
def inicio_vista(request):
    # obtener todos los registros de la tabla Materia
    ListadoCatalogo=Catalogo.objects.all()
    return render(request,"gestionarCatalogo.html",{"loscatalogos":ListadoCatalogo})
