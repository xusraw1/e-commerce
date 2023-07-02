from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, UpdateProductForm
from .models import ProductImage, Product, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


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
    product = get_object_or_404(Product, id=product_id)

    if 'recently_viewed' in request.session:
        r_viewed = request.session['recently_viewed']
        if not product.id in r_viewed:
            r_viewed.append(product.id)
            request.session.modified = True
    else:
        request.session["recently_viewed"] = [product.id, ]

    return render(request, "product_detail.html", {'product': product})


@login_required(login_url='login')
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user == product.author:
        if request.method == 'GET':
            form = UpdateProductForm(instance=product)
            return render(request, 'update_product.html', {'form': form, 'product': product})
        elif request.method == 'POST':
            form = UpdateProductForm(instance=product, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                if request.FILES.getlist('images'):
                    ProductImage.objects.filter(product=product).delete()
                    for i in request.FILES.getlist('images'):
                        ProductImage.objects.create(product=product, image=i)
                return redirect('product', product.id)
            return render(request, 'update_product.html', {'form': form, 'product': product})
    else:
        messages.error(request, 'Acess danied!')
        return redirect('commerce:index')


@login_required(login_url='login')
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user == product.author:
        if request.method == 'POST':
            product.delete()
            messages.info(request, "Product deleted successfully!")
            return redirect('commerce:index')
        else:
            return render(request, 'product_delete.html', {'product': product})
    else:
        messages.error(request, "You can`t delete product, because you don`t author for this prodcut!")
        return redirect('commerce:index')


@login_required(login_url='login')
def new_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            author=request.user,
            product=product,
            text=request.POST['body']
        )
        messages.info(request, "Comment successfully sended!")
        return redirect('product', product_id)
    else:
        return HttpResponse("add comment")


@login_required(login_url='login')
def delete_comment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
        messages.info(request, "Comment successfully deleted!")
        return redirect('product', product_id)
    return redirect('product', product_id)
