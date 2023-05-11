"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Models.testing4.views import formulariofacturaview,formularioproductoview,formulariofacturadetalleview,formularioclienteview,formulariousuarioview
from View.homeview import Homeview

urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', Homeview.home, name='home'),
    path('pagina/', Homeview.pag1, name='pag1'),
    path('factura/', Homeview.factura, name='factura'),
    path('registrofactura/', formulariofacturaview.index, name='registrofactura'),
    path('guardarfactura/', formulariofacturaview.procesar_factura, name='guardarfactura'),
    path('registroproducto/', formularioproductoview.index, name='registroproducto'),
    path('guardarproducto/', formularioproductoview.procesar_producto, name='guardarproducto'),
    path('registrousuario/', formulariousuarioview.index, name='registrousuario'),
    path('guardarusuario/', formulariousuarioview.procesar_usuario, name='guardarusuario'),
    path('registrocliente/', formularioclienteview.index, name='registrocliente'),
    path('guardarcliente/', formularioclienteview.procesar_cliente, name='guardarcliente'),
    path('registrofacturadetalle/', formulariofacturadetalleview.index, name='registrofacturadetalle'),
    path('guardarfacturadetalle/', formulariofacturadetalleview.procesar_facturadetalle, name='guardarfacturadetalle'),
    path('listarfactura/', formulariofacturaview.listar_factura, name='listarfactura'),
    path('listarproducto/', formularioproductoview.listar_producto, name='listarproducto'),
    path('listarusuario/', formulariousuarioview.listar_usuario, name='listarusuario'),
    path('listarcliente/', formularioclienteview.listar_cliente, name='listarcliente'),
    path('listarfacturadetalle/', formulariofacturadetalleview.listar_detalle, name='listardetalle'),
    path('editfactura/<int:id_factura>', formulariofacturaview.edit_factura, name='editfactura'),
    path('actualizarfactura/<int:id_factura>', formulariofacturaview.actualizar_factura, name='actualizarfactura'),
    path('editusuario/<int:id_usuario>', formulariousuarioview.edit_usuario, name='editusuario'),
    path('actualizarusuario/<int:id_usuario>', formulariousuarioview.actualizar_usuario, name='actualizarusuario'),
    path('editcliente/<int:id_cliente>', formularioclienteview.edit_cliente, name='editcliente'),
    path('actualizarcliente/<int:id_cliente>', formularioclienteview.actualizar_cliente, name='actualizarcliente'),
    path('editdetalle/<int:id_detalle>', formulariofacturadetalleview.edit_detalle, name='editdetalle'),
    path('actualizardetalle/<int:id_detalle>', formulariofacturadetalleview.actualizar_detalle, name='actualizardetalle'),
    path('editproducto/<int:id_producto>', formularioproductoview.edit_producto, name='editproducto'),
    path('actualizarproducto/<int:id_producto>', formularioproductoview.actualizar_producto, name='actualizarproducto'),
    path('eliminarfactura/<int:id_factura>', formulariofacturaview.eliminar_factura, name='eliminarfactura'),
    path('eliminarusuario/<int:id_usuario>', formulariousuarioview.eliminar_usuario, name='eliminarusuario'),
    path('eliminarproducto/<int:id_producto>', formularioproductoview.eliminar_producto, name='eliminarproducto'),
    path('eliminardetalle/<int:id_detalle>', formulariofacturadetalleview.eliminar_detalle, name='eliminardetalle'),
    path('eliminarcliente/<int:id_cliente>', formularioclienteview.eliminar_cliente, name='eliminarcliente'),

]
