from django.shortcuts import render

# Sayfaya mesaj göndermek için
from django.contrib import messages

#Kullanıcılar tablosuna erişmek için
from django.contrib.auth.models import User

#Giriş işlemi için
from django.contrib.auth import login,logout,authenticate

# Yönlendirme işlemleri için
from django.shortcuts import redirect

# Create your views here.

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('anasayfa')
        else:
            messages.error(request,"Kullanıcı bulunamadı")
            return render(request,'login.html')


    return render(request,"login.html")

def register_view(request):
    #veri var mı diye kontrol eder
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")

        if password!=password2:
            messages.warning(request,"Şifreler eşleşmiyor.Gözlerini baktır 😂")
            return render(request,"register.html")
        if User.objects.filter(username=username).exists():
            messages.warning(request,"Aynı kullanıcı adı zaten alınmış 😉")
            return render(request,"register.html")
        newuser=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        newuser.save()
        return redirect("login")

    return render(request,"register.html")

def logout_view(request):
    logout(request)
    return redirect('login')
