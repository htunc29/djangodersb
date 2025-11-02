from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="urunler")
]
# http://127.0.0.1:8000/urunler/

