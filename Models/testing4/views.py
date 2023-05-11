from django.http import HttpRequest
from django.shortcuts import render
from Models.testing4.form import factura, cliente, producto, detalle_factura, usuario
from Models.testing4.form import formulariofactura, formulariousuario, formulariocliente, formulariodetalle_factura, \
    formularioproducto
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
class formulariofacturaview(HttpRequest):
    def index(request):
        factura = formulariofactura()
        return render(request, "facturaindex.html", {"form": factura})

    def procesar_factura(request):
        factura = formulariofactura(request.POST)
        if factura.is_valid():
            factura.save()
            factura = formulariofactura()
        return render(request, "facturaindex.html", {"form": factura, "mensaje": 'OK'})

    def listar_factura(request):
        factura1 = factura.objects.all()
        return render(request, "listarfactura.html", {"factura1": factura1})

    def edit_factura(request, id_factura):
        factura1 = factura.objects.filter(id=id_factura).first()
        form = formulariofactura(instance=factura1)
        return render(request, "facturaedit.html", {"form": form, 'factura1': factura1})

    def actualizar_factura(request, id_factura):
        factura1 = factura.objects.get(pk=id_factura)
        form = formulariofactura(request.POST, instance=factura1)
        if form.is_valid():
            form.save()
        factura1 = factura.objects.all()
        return render(request, "listarfactura.html", {"factura1": factura1})

    def eliminar_factura(request, id_factura):
        factura1 = factura.objects.get(pk=id_factura)
        factura1.delete()
        factura1 = factura.objects.all()
        return render(request, "listarfactura.html", {"factura1": factura1})


class formulariousuarioview(HttpRequest):
    def index(request):
        usuario = formulariousuario()
        return render(request, "usuarioindex.html", {"form": usuario})

    def procesar_usuario(request):
        usuario = formulariousuario(request.POST)
        if usuario.is_valid():
            usuario.save()
            usuario = formulariousuario()
        return render(request, "usuarioindex.html", {"form": usuario, "mensaje": 'OK'})

    def listar_usuario(request):
        usuario1 = usuario.objects.all()
        return render(request, "listarusuario.html", {"usuario1": usuario1})

    def edit_usuario(request, id_usuario):
        usuario1 = usuario.objects.filter(id=id_usuario).first()
        form = formulariousuario(instance=usuario1)
        return render(request, "usuarioedit.html", {"form": form, 'usuario1': usuario1})

    def actualizar_usuario(request, id_usuario):
        usuario1 = usuario.objects.get(pk=id_usuario)
        form = formulariousuario(request.POST, instance=usuario1)
        if form.is_valid():
            form.save()
        usuario1 = usuario.objects.all()
        return render(request, "listarusuario.html", {"usuario1": usuario1})

    def eliminar_usuario(request, id_usuario):
        usuario1 = usuario.objects.get(pk=id_usuario)
        usuario1.delete()
        usuario1 = usuario.objects.all()
        return render(request, "listarusuario.html", {"usuario1": usuario1})


class formularioclienteview(HttpRequest):
    def index(request):
        cliente = formulariocliente()
        return render(request, "clienteindex.html", {"form": cliente})

    def procesar_cliente(request):
        cliente = formulariocliente(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = formulariocliente()
        return render(request, "clienteindex.html", {"form": cliente, "mensaje": 'OK'})

    def listar_cliente(request):
        cliente1 = cliente.objects.all()
        return render(request, "listarcliente.html", {"cliente1": cliente1})

    def edit_cliente(request, id_cliente):
        cliente1 = cliente.objects.filter(id=id_cliente).first()
        form = formulariocliente(instance=cliente1)
        return render(request, "clienteedit.html", {"form": form, 'cliente1': cliente1})

    def actualizar_cliente(request, id_cliente):
        cliente1 = cliente.objects.get(pk=id_cliente)
        form = formulariocliente(request.POST, instance=cliente1)
        if form.is_valid():
            form.save()
        cliente1 = cliente.objects.all()
        return render(request, "listarcliente.html", {"cliente1": cliente1})

    def eliminar_cliente(request, id_cliente):
        cliente1 = cliente.objects.get(pk=id_cliente)
        cliente1.delete()
        cliente1 = cliente.objects.all()
        return render(request, "listarcliente.html", {"cliente1": cliente1})


class formulariofacturadetalleview(HttpRequest):
    def index(request):
        facturadetalle = formulariodetalle_factura()
        return render(request, "facturadetalleindex.html", {"form": facturadetalle})

    def procesar_facturadetalle(request):
        facturadetalle = formulariodetalle_factura(request.POST)
        if facturadetalle.is_valid():
            facturadetalle.save()
            facturadetalle = formulariodetalle_factura()
        return render(request, "facturadetalleindex.html", {"form": facturadetalle, "mensaje": 'OK'})

    def listar_detalle(request):
        detalle1 = detalle_factura.objects.all()
        return render(request, "listarfacturadetalle.html", {"detalle1": detalle1})

    def edit_detalle(request, id_detalle):
        detalle1 = detalle_factura.objects.filter(id=id_detalle).first()
        form = formulariodetalle_factura(instance=detalle1)
        return render(request, "detalleedit.html", {"form": form, 'detalle1': detalle1})

    def actualizar_detalle(request, id_detalle):
        detalle1 = detalle_factura.objects.get(pk=id_detalle)
        form = formulariodetalle_factura(request.POST, instance=detalle1)
        if form.is_valid():
            form.save()
        detalle1 = detalle_factura.objects.all()
        return render(request, "listarfacturadetalle.html", {"detalle1": detalle1})

    def eliminar_detalle(request, id_detalle):
        detalle1 = detalle_factura.objects.get(pk=id_detalle)
        detalle1.delete()
        detalle1 = detalle_factura.objects.all()
        return render(request, "listarfacturadetalle.html", {"detalle1": detalle1})


class formularioproductoview(HttpRequest):
    def index(request):
        producto = formularioproducto()
        return render(request, "productoindex.html", {"form": producto})

    def procesar_producto(request):
        producto = formularioproducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = formularioproducto()
        return render(request, "productoindex.html", {"form": producto, "mensaje": 'OK'})

    def listar_producto(request):
        producto1 = producto.objects.all()
        return render(request, "listarproducto.html", {"producto1": producto1})

    def edit_producto(request, id_producto):
        producto1 = producto.objects.filter(id=id_producto).first()
        form = formularioproducto(instance=producto1)
        return render(request, "productoedit.html", {"form": form, 'producto1': producto1})

    def actualizar_producto(request, id_producto):
        producto1 = producto.objects.get(pk=id_producto)
        form = formularioproducto(request.POST, instance=producto1)
        if form.is_valid():
            form.save()
        producto1 = producto.objects.all()
        return render(request, "listarproducto.html", {"producto1": producto1})

    def eliminar_producto(request, id_producto):
        producto1 = producto.objects.get(pk=id_producto)
        producto1.delete()
        producto1 = producto.objects.all()
        return render(request, "listarproducto.html", {"producto1": producto1})
