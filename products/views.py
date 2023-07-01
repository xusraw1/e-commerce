from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, UpdateProductForm
from .models import ProductImage, Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
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
@login_required(login_url='login')
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user == product.author:
        if request.method == 'GET':
            form = UpdateProductForm(instance=product)
            return render(request, 'update_product.html', {'form': form, 'product': product})
        elif request.method == 'POST':
            form = UpdateProductForm(intance=product, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                if request.FILES.getlist['images']:
                    ProductImage.objects.filter(product=product).delete()
                    for i in request.FILES.getlist['images']:
                        ProductImage.objects.create(product=product, image=i)
                return redirect('product', product.id)
            return render(request, 'update_product.html', {'form': form, 'product': product})
    else:
        messages.error(request, 'Acess danied!')
        return redirect('commerce:index')
