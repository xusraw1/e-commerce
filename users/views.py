from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views import View
from django.contrib import messages


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