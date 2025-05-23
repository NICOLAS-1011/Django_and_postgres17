from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_motos, name='lista_motos'),
    path('crear/', views.crear_moto, name='crear_moto'),
    path('editar/<int:id>/', views.editar_moto, name='editar_moto'),
    path('eliminar/<int:id>/', views.eliminar_moto, name='eliminar_moto'),

    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),

    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    #path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/editar/<int:id>/', views.actualizar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    path('empleados/', views.lista_empleado, name='lista_empleado'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', views.eliminar_empleado, name='eliminar_empleado'),

    path('ventas/', views.lista_ventas, name='lista_ventas'),
    #path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/crear/', views.registrar_venta, name='crear_venta'),
    path('ventas/editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    #path('ventas/eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),
    path('ventas/eliminar/<int:pk>/', views.eliminar_venta, name='eliminar_venta'),


]