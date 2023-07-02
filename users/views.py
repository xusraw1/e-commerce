from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, UpdateProfile
from django.views import View
from django.contrib import messages
from .models import CustomUser, Saved
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from products.models import Product


class SignUpView(UserPassesTestMixin, View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You account is successfully created!!!")
            return redirect('login')
        else:
            return render(request, 'registration/signup.html', {"form": form})

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        else:
            return True


class Profile(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', context={
            'user': user
        })


class UpdateProfileView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = UpdateProfile(instance=request.user)
        return render(request, 'profile_update.html', {'form': form})

    def post(self, request):
        form = UpdateProfile(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You account is successfully updated!!!")
            return redirect('profile', request.user.username)
        else:
            return render(request, 'registration/signup.html', {"form": form})


class AddRemoveSavedView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_product = Saved.objects.filter(author=request.user, product=product)
        if saved_product:
            saved_product.delete()
            messages.info(request, "Removed.")
        else:
            Saved.objects.create(author=request.user, product=product)
        return redirect(request.Meta.get('HTTP_REFERER'))


class SavedView(LoginRequiredMixin, View):
    def get(self, request):
        saveds = Saved.objects.filter(author=request.user)
        q = request.GET['q']
        if q:
            products = Product.objects.filter(title__icontains=q)
            saveds = Saved.objects.filter(products__in=products, author=request.user)
        return render(request, 'saved.html', {'saveds': saveds})


class RecentlyViewed(View):
    def get(self, request):
        if not "recently_viewed" in request.session:
            products = []
        else:
            r_viewed = request.session["recently_viewed"]
            products = Product.objects.filter(id__in=r_viewed)
            q = request.GET['q']
            if q:
                products = products.filter(title__icontains=q)
        return render(request, "recently.html", {'products': products})
