from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, UpdateProfile
from django.views import View
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

    def test_fucn(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        else:
            True


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
