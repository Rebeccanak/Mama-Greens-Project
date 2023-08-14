from django import forms
from Cart.models import Cart

class CartUploadForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
