from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_empresa


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cilindraje = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Venta(models.Model):
    fecha_venta = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    forma_pago = models.CharField(max_length=50, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    placa =models.CharField(max_length=20)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha_venta}"


class AuditoriaVenta(models.Model):
    venta_id = models.IntegerField()
    fecha_venta = models.DateField()
    cliente_id = models.IntegerField()
    empleado_id = models.IntegerField()
    moto_id = models.IntegerField()
    forma_pago = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_eliminacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Auditoría Venta ID {self.venta_id} eliminada el {self.fecha_eliminacion}"
