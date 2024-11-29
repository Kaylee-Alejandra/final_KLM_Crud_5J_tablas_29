from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados= Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"misempleados":losempleados}) 

def registrarEmpleado (request):
    
    id_empleado= request.POST["numid_empleado"]
    nombre= request.POST["txtnombre"]
    direccion= request.POST["txtdireccion"]
    puesto= request.POST["txtpuesto"]
    sueldo= request.POST["numsueldo"]
    telefono= request.POST["numtelefono"]
    correo= request.POST["txtcorreo"]

    guardarEmpleado=Empleado.objects.create(
        id_empleado=id_empleado, nombre=nombre,direccion=direccion, puesto=puesto,sueldo=sueldo,telefono=telefono,correo=correo
    )   # GUARDA EL REGISTRO 

    return redirect("empleados")

def seleccionarEmpleado(request, id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"misempleados": empleado})



def editarEmpleado(request):
        id_empleado= request.POST["numid_empleado"]
        nombre= request.POST["txtnombre"]
        direccion= request.POST["txtdireccion"]
        puesto= request.POST["txtpuesto"]
        sueldo= request.POST["numsueldo"]
        telefono= request.POST["numtelefono"]
        correo= request.POST["txtcorreo"]
        empleado=Empleado.objects.get(id_empleado=id_empleado)
        empleado.nombre=nombre
        empleado.direccion=direccion
        empleado.puesto=puesto
        empleado.sueldo=sueldo
        empleado.telefono=telefono
        empleado.correo=correo
        
        empleado.save() #guardar registro actualizado 
        return redirect("empleados")

def borrarEmpleado(request, id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete() #borra el registro
    return redirect("empleados")