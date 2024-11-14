from django.shortcuts import render,redirect
from .models import inventario
# Create your views here.

def inicio_vista(request):
    inventario = inventario.objects.all()
    return render(request,"gestionarinventario.html",{"Misproductos":inventario})

def registrarinventario(request):
    id_inventario = request.POST["txtinventario"]
    kilos_de_carne = request.POST["numkilos-de-carne"]
    tipos_de_carne = request.POST["txttipos-de-carne"]
    tipos_de_salsa = request.POST["txttipos-de-carne"]
    tortillas = request.POST["txttipos-de-carne"]
    verduras = request.POST["txttipos-de-carne"]
    desechables = request.POST["txttipos-de-carne"]

    guardarinventario = inventario.objects.create(id_inventario=id_inventario,kilos_de_carne,tipos_de_carne,tipos_de_salsa,tortillas,verduras,desechables)
    return redirect("/")

def seleccionarproducto(request,id-inventario):
    inventario=inventario.objects.get(id_inventario=id-inventario)
    return render(request,"editarproducto.html",{"misproductos":inventario})


def editarProducto(request):
    id_inventario = request.POST["txtinventario"]
    kilos_de_carne = request.POST["numkilos-de-carne"]
    tipos_de_carne = request.POST["txttipos-de-carne"]
    tipos_de_salsa = request.POST["txttipos-de-carne"]
    tortillas = request.POST["txttipos-de-carne"]
    verduras = request.POST["txttipos-de-carne"]
    desechables = request.POST["txttipos-de-carne"]
    materia=Materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos=creditos
    materia.save()

    return redirect("/")

def borrarProducto(request, codigo):
    inventario=inventario.objects.get(codigo=codigo)
    producto.delete()

    return redirect("/")