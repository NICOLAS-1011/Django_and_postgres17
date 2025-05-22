from django.shortcuts import render, redirect, get_object_or_404
from .models import Moto
from .models import Proveedor
from .models import Cliente
from .models import Empleado
from .models import Venta
from .forms import MotoForm
from .forms import ProveedorForm
from .forms import ClienteForm
from .forms import EmpleadoForm
from .forms import VentaForm


#MOTOS 

def lista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/lista_motos.html', {'motos': motos})

def crear_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotoForm()
    return render(request, 'motos/form_moto.html', {'form': form, 'accion': 'Crear'})

def editar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)
    if request.method == 'POST':
        form = MotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('lista_motos')
    else:
        form = MotoForm(instance=moto)
    return render(request, 'motos/form_moto.html', {'form': form, 'accion': 'Editar'})

def eliminar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)
    if request.method == 'POST':
        moto.delete()
        return redirect('lista_motos')
    return render(request, 'motos/confirmar_eliminar.html', {'moto': moto})


#PROVEEDORES

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/lista.html', {'proveedores': proveedores})


def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'proveedores/formulario.html', {'form': form})


def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/formulario.html', {'form': form})


def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'proveedores/confirmar_eliminar.html', {'proveedor': proveedor})


#CLIENTES

# Listar
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista.html', {'clientes': clientes})

# Crear
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/crear.html', {'form': form})

# Editar
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/editar.html', {'form': form})

# Eliminar
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('listar_clientes')


#EMPLEADOS

def lista_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/lista.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado/formulario.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/formulario.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'empleado/confirmar_eliminar.html', {'empleado': empleado})


#VENTAS

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/lista.html', {'ventas': ventas})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm()
    return render(request, 'venta/formulario.html', {'form': form})

def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'venta/formulario.html', {'form': form})

def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('lista_ventas')
    return render(request, 'venta/confirmar_eliminar.html', {'venta': venta})
