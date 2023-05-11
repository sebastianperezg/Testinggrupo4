from django.http import HttpResponse
from django.template.loader import get_template


class Homeview():
    def home(self):
        plantilla=get_template('index.html')
        return HttpResponse(plantilla.render())
    def pag1(self):
        return HttpResponse('hola2')

    def factura(self):
        plantilla = get_template('factura.html')
        return HttpResponse(plantilla.render())