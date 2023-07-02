from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import Product, Category


def get_category(request):
    categories = Category.objects.all()
    return {'categories': categories}


class IndexView(View):

    def get(self, request):
        products = Product.objects.all()
        q = request.GET['q']
        if q:
            products = products.filter(title__icontains=q)
        return render(request, 'index.html', {'products': products})


class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
