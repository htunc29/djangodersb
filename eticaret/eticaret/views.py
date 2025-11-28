from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request,"eticaret/home.html",)


def category(request,kategori_adi):
    return render(request,"eticaret/kategori.html",{
        "kategori":kategori_adi
    })
