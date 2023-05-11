from django.db import models

class factura(models.Model):
    id_factura=models.CharField(max_length=10)
    fecha_emision=models.CharField(max_length=50)
    id_cliente=models.CharField(max_length=10)
    estado=models.CharField(max_length=50)
    total=models.CharField(max_length=50)

class detalle_factura(models.Model):
    id_factura=models.CharField(max_length=10)
    id_producto=models.CharField(max_length=10)
    cantidad_producto=models.CharField(max_length=50)
    precio_unitario=models.DecimalField

class cliente(models.Model):
    id_cliente=models.CharField(max_length=10)
    dni=models.CharField(max_length=8)
    nombre=models.CharField(max_length=50)
    ruc_cliente=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

class producto(models.Model):
    id_producto=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField
    cantidad_stock=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)

class usuario(models.Model):
    id_usuario=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    rol=models.CharField(max_length=20)