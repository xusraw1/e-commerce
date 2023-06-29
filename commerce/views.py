from django.shortcuts import render
from django.views import View
from products.models import Product


class IndexView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})


