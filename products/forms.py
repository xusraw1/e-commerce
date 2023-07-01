from .models import Product
from django import forms


class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={}), required=False)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'address', 'category', 'number', 'telegram']

    def save(self, request, commit=True):
        product = self.instance
        product.author = request.user
        super().save(commit)
        return product