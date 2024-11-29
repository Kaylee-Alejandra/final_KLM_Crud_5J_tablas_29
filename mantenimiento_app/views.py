from django.shortcuts import render, redirect
from .models import Mantenimiento
# Create your views here.
def inicio_vistaMantenimiento(request):
    losmantenimiento= Mantenimiento.objects.all()
    return render(request, "gestionarMantenimiento.html", {"mismantenimiento":losmantenimiento}) 

def registrarMantenimiento (request):
    id_mantenimiento= request.POST["numid_mantenimiento"]
    horarios= request.POST["txthorarios"]
    pisos= request.POST["txtpisos"]
    instrumentos= request.POST["txtinstrumentos"]
    oficinas= request.POST["txtoficinas"]
    empleados= request.POST["txtempleados"]
    materiales= request.POST["txtmateriales"]

    guardarMantenimiento=Mantenimiento.objects.create(
        id_mantenimiento=id_mantenimiento,horarios=horarios,pisos=pisos,instrumentos=instrumentos,oficinas=oficinas,empleados=empleados,materiales=materiales
    )   # GUARDA EL REGISTRO 

    return redirect("mantenimiento")

def seleccionarMantenimiento(request, id_mantenimiento):
    mantenimiento=Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    return render(request, "editarMantenimiento.html", {"mismantenimiento": mantenimiento})

def editarMantenimiento(request):
        id_mantenimiento= request.POST["numid_mantenimiento"]
        horarios= request.POST["txthorarios"]
        pisos= request.POST["txtpisos"]
        instrumentos= request.POST["txtinstrumentos"]
        oficinas= request.POST["txtoficinas"]
        empleados= request.POST["txtempleados"]
        materiales= request.POST["txtmateriales"]
        mantenimiento=Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
        mantenimiento.horarios=horarios
        mantenimiento.pisos=pisos
        mantenimiento.instrumentos=instrumentos
        mantenimiento.oficinas=oficinas
        mantenimiento.empleados=empleados
        mantenimiento.materiales=materiales
        
        mantenimiento.save() #guardar registro actualizado 
        return redirect("mantenimiento")

def borrarMantenimiento(request, id_mantenimiento):
    mantenimiento=Mantenimiento.objects.get(id_mantenimiento=id_mantenimiento)
    mantenimiento.delete() #borra el registro
    return redirect("mantenimiento")
