from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from django.views import View
from django.contrib import messages
from .models import CustomUser


class SignUpView(View):
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


class Profile(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'profile.html', context={
            'user': user
        })
