from django import forms

from Models.testing4.models import factura, usuario, cliente, detalle_factura, producto

class formulariofactura(forms.ModelForm):
    class Meta:
        model = factura
        fields = '__all__'

class formulariousuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'

class formulariocliente(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class formulariodetalle_factura(forms.ModelForm):
    class Meta:
        model = detalle_factura
        fields = '__all__'

class formularioproducto(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

