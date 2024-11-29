from django.shortcuts import render, redirect
from .models import Instrumento
# Create your views here.
def inicio_vistaInstrumento(request):
    losinstrumentos= Instrumento.objects.all()
    return render(request, "gestionarInstrumento.html", {"misinstrumentos":losinstrumentos}) 

def registrarInstrumento (request):
    
    codigo= request.POST["numcodigo"]
    tipo_instrumento= request.POST["txttipo_instrumento"]
    color= request.POST["txtcolor"]
    marca= request.POST["txtmarca"]
    precio= request.POST["numprecio"]
    nombre= request.POST["txtnombre"]
    tamaño= request.POST["txttamaño"]

    guardarinstrumento=Instrumento.objects.create(
        codigo=codigo, tipo_instrumento=tipo_instrumento,color=color,marca=marca,precio=precio,nombre=nombre,tamaño=tamaño
    )   # GUARDA EL REGISTRO 

    return redirect("instrumentos")

def seleccionarInstrumentos(request, codigo):
    instrumento=Instrumento.objects.get(codigo=codigo)
    return render(request, "editarInstrumento.html", {"misinstrumentos": instrumento})



def editarInstrumento(request):
        codigo= request.POST["numcodigo"]
        tipo_instrumento= request.POST["txttipo_instrumento"]
        color= request.POST["txtcolor"]
        marca= request.POST["txtmarca"]
        precio= request.POST["numprecio"]
        nombre= request.POST["txtnombre"]
        tamaño= request.POST["txttamaño"]
        instrumento=Instrumento.objects.get(codigo=codigo)
        instrumento.tipo_instrumento=tipo_instrumento
        instrumento.color=color
        instrumento.marca=marca
        instrumento.precio=precio
        instrumento.nombre=nombre
        instrumento.tamaño=tamaño
        
        instrumento.save() #guardar registro actualizado 
        return redirect("instrumentos")

def borrarInstrumento(request, codigo):
    instrumento=Instrumento.objects.get(codigo=codigo)
    instrumento.delete() #borra el registro
    return redirect("instrumentos")