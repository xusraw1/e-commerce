from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import ProductImage, Product
from django.contrib import messages


def new_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_new.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(request)
            for image in request.FILES.getlist("images"):
                ProductImage.objects.create(image=image, product=product)
            messages.success(request, "Successfully created!")
            return redirect('commerce:index')
        return render(request, "product_new.html", {'form': form})


def detail_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_detail.html", {'product': product})
