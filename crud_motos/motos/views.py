from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection, DatabaseError
from django.contrib import messages
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


def index(request):
    return render(request, 'indice/principal.html')

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
    moto = Moto.objects.get(id=id)
    moto.delete()
    return redirect('lista_motos')
    

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
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('listar_proveedores')
    



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
#def editar_cliente(request, id):
#    cliente = Cliente.objects.get(id=id)
#    if request.method == 'POST':
#        form = ClienteForm(request.POST, instance=cliente)
#        if form.is_valid():
#            form.save()
#            return redirect('listar_clientes')
#    else:
#        form = ClienteForm(instance=cliente)
#    return render(request, 'cliente/editar.html', {'form': form})

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
            return redirect('lista_empleado')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado/formulario.html', {'form': form})

def eliminar_empleado(request, pk):
    empleado = Empleado.objects.get(pk=pk)
    empleado.delete()
    return redirect('lista_empleado')
  
      

#VENTAS

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/lista.html', {'ventas': ventas})

#def crear_venta(request):
#    if request.method == 'POST':
#        form = VentaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('lista_ventas')
#    else:
#        form = VentaForm()
#    return render(request, 'venta/formulario.html', {'form': form})

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

#def eliminar_venta(request, pk):
#    venta = get_object_or_404(Venta, pk=pk)
#    if request.method == 'POST':
#        venta.delete()
#        return redirect('lista_ventas')
#    return render(request, 'venta/confirmar_eliminar.html', {'venta': venta})


#PROCEDIMIENTOS

def registrar_venta(request):
    if request.method == 'POST':
        fecha_venta = request.POST.get('fecha_venta')
        id_cliente = request.POST.get('cliente')
        id_empleado = request.POST.get('empleado')
        id_moto = request.POST.get('moto')
        forma_pago = request.POST.get('forma_pago')
        valor_total = request.POST.get('valor_total')

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "CALL registrar_venta(%s, %s, %s, %s, %s, %s)",
                    [fecha_venta, id_cliente, id_empleado, id_moto, forma_pago, valor_total]
                )
            return redirect('lista_ventas')
        except DatabaseError as e:
            error_msg = str(e)
            clientes = Cliente.objects.all()
            empleados = Empleado.objects.all()
            motos = Moto.objects.filter(estado__iexact='disponible')
            return render(request, 'venta/registrar_venta.html', {
                'clientes': clientes,
                'empleados': empleados,
                'motos': motos,
                'error': error_msg
            })
    
    else:  # GET
        clientes = Cliente.objects.all()
        empleados = Empleado.objects.all()
        motos = Moto.objects.filter(estado__iexact='disponible')  # solo motos disponibles
        return render(request, 'venta/registrar_venta.html', {
            'clientes': clientes,
            'empleados': empleados,
            'motos': motos
        })


def eliminar_venta(request, pk):
    try:
        # Validamos que exista la venta
        venta = get_object_or_404(Venta, pk=pk)

        with connection.cursor() as cursor:
            cursor.execute("CALL eliminar_venta(%s)", [pk])
        return redirect('lista_ventas')

    except DatabaseError as e:
        print(f"Error al eliminar la venta con ID {pk}: {e}")
        return redirect('lista_ventas')

  

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CALL actualizar_cliente(%s, %s, %s, %s, %s, %s, %s);
                """, [id, nombre, apellido, cedula, telefono, correo, direccion])
            return redirect('listar_clientes')
        except DatabaseError as e:
            print(f"Error al actualizar el cliente con ID {id}: {e}")
            return redirect('listar_clientes')

    return render(request, 'cliente/editar_cliente.html', {'cliente': cliente})