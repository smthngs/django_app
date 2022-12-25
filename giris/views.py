from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def giris_view(request):
    mevcutsayfa = "3"
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect("/", {"mevcutsayfa": "2"})

    return render(request, "giris.html", {"mevcutsayfa": mevcutsayfa, "form": form})


def hesapolustur_view(request):
    mevcutsayfa = "4"
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        login(request, user)
        messages.success(request, "Hesap oluşturma başarılı.")
        return HttpResponseRedirect("/", {"mevcutsayfa": "2"})

    return render(request, "hesapolustur.html", {"mevcutsayfa": mevcutsayfa, "form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/", {"mevcutsayfa": "2"})
