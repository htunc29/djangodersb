# Django Dersi - Kullanıcılar App ve Template Kullanımı

Bu derste Django'da yeni bir uygulama oluşturmayı, template'lerle çalışmayı ve temel Django özelliklerini öğreneceğiz.

## Ders İçeriği

### 1. Kullanıcılar App Oluşturma
Django'da yeni bir uygulama oluşturma:
```bash
python manage.py startapp kullanicilar
```

Uygulamayı `settings.py` dosyasına ekleme:
```python
INSTALLED_APPS = [
    # ...
    'kullanicilar',
]
```

### 2. Kullanıcılar Sayfası (.html) Oluşturma ve Render Etme
- `kullanicilar/templates/kullanicilar/` klasör yapısı oluşturma
- HTML sayfası hazırlama
- `views.py` içinde view fonksiyonu yazma
- `render()` fonksiyonu ile template'i döndürme

**Örnek View:**
```python
from django.shortcuts import render

def kullanicilar_listesi(request):
    return render(request, 'kullanicilar/liste.html')
```

### 3. Sayfaya Link Verme ve Yönlendirmeler - path(name="")
- `urls.py` dosyasında URL pattern tanımlama
- `name` parametresi ile URL'e isim verme
- Template'lerde `{% url 'isim' %}` kullanımı

**Örnek URL Pattern:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('kullanicilar/', views.kullanicilar_listesi, name='kullanicilar_listesi'),
]
```

**Template'de Link Kullanımı:**
```html
<a href="{% url 'kullanicilar_listesi' %}">Kullanıcılar Sayfası</a>
```

### 4. Sayfaya Context ile Veri Gönderme
View'dan template'e veri aktarma:

```python
def kullanicilar_listesi(request):
    context = {
        'baslik': 'Kullanıcılar Listesi',
        'toplam_kullanici': 150
    }
    return render(request, 'kullanicilar/liste.html', context)
```

### 5. Sayfada Context ile Gönderilen Veriyi Görüntüleme
Template'de context değişkenlerini kullanma:

```html
<h1>{{ baslik }}</h1>
<p>Toplam Kullanıcı Sayısı: {{ toplam_kullanici }}</p>
```

### 6. Sayfada {{for}} Kullanımı (Dummy Ürün Listesi)
Liste halindeki verileri template'de görüntüleme:

**View:**
```python
def kullanicilar_listesi(request):
    kullanicilar = [
        {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 25},
        {'ad': 'Ayşe', 'soyad': 'Kaya', 'yas': 30},
        {'ad': 'Mehmet', 'soyad': 'Demir', 'yas': 28},
    ]
    context = {
        'kullanicilar': kullanicilar
    }
    return render(request, 'kullanicilar/liste.html', context)
```

**Template:**
```html
<ul>
{% for kullanici in kullanicilar %}
    <li>{{ kullanici.ad }} {{ kullanici.soyad }} - {{ kullanici.yas }} yaşında</li>
{% endfor %}
</ul>
```

### 7. Sayfada {{if}} Kullanımı (Olup Olmama Durumları)
Koşullu içerik gösterme:

```html
{% if kullanicilar %}
    <p>Toplam {{ kullanicilar|length }} kullanıcı bulundu.</p>
    <ul>
    {% for kullanici in kullanicilar %}
        <li>
            {{ kullanici.ad }}
            {% if kullanici.yas >= 30 %}
                <span class="badge">Kıdemli</span>
            {% else %}
                <span class="badge">Genç</span>
            {% endif %}
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>Henüz kullanıcı bulunmamaktadır.</p>
{% endif %}
```

### 8. Django Tagleri
Sık kullanılan Django template tagleri:

#### Değişken Gösterme
```html
{{ degisken }}
{{ degisken.alan }}
{{ liste.0 }}
```

#### URL Tag
```html
{% url 'url-adi' %}
{% url 'url-adi' parametre %}
```

#### Static Dosyalar
```html
{% load static %}
<img src="{% static 'images/logo.png' %}">
```

#### For Loop
```html
{% for item in liste %}
    {{ item }}
{% empty %}
    Liste boş
{% endfor %}
```

#### If-Elif-Else
```html
{% if kosul1 %}
    ...
{% elif kosul2 %}
    ...
{% else %}
    ...
{% endif %}
```

#### Filters (Filtreler)
```html
{{ metin|upper }}
{{ tarih|date:"d/m/Y" }}
{{ liste|length }}
{{ sayi|add:5 }}
{{ metin|truncatewords:10 }}
```

#### Include
```html
{% include 'parcali_template.html' %}
{% include 'parcali_template.html' with degisken=deger %}
```

#### Block ve Extends (Kalıtım)
```html
<!-- base.html -->
{% block content %}{% endblock %}

<!-- child.html -->
{% extends 'base.html' %}
{% block content %}
    İçerik buraya
{% endblock %}
```

### 9. Fake User Control (Kullanıcı Kontrolü)
Template'de kullanıcı durumunu kontrol etme:

```html
{% if user.is_authenticated %}
    <p>Hoş geldin, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Çıkış Yap</a>
{% else %}
    <p>Lütfen giriş yapın.</p>
    <a href="{% url 'login' %}">Giriş Yap</a>
{% endif %}
```

**Kullanıcı Yetki Kontrolü:**
```html
{% if user.is_staff %}
    <a href="{% url 'admin:index' %}">Admin Panel</a>
{% endif %}

{% if user.is_superuser %}
    <button>Özel İşlem</button>
{% endif %}
```

## Proje Yapısı
```
djangokurs/
├── eticaret/
│   ├── eticaret/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   └── kullanicilar/
│       ├── templates/
│       │   └── kullanicilar/
│       │       └── liste.html
│       ├── views.py
│       ├── urls.py
│       └── ...
└── sanalortam/
```

## Çalıştırma
```bash
# Sanal ortamı aktifleştir
source sanalortam/bin/activate  # Linux/Mac
sanalortam\Scripts\activate     # Windows

# Geliştirme sunucusunu başlat
cd eticaret
python manage.py runserver
```

## Önemli Notlar
- Template dosyaları mutlaka `templates/uygulama_adi/` klasör yapısında olmalı
- Static dosyalar için `{% load static %}` kullanılmalı
- URL pattern'lerde `name` parametresi kullanmak best practice'dir
- Context dictionary kullanarak view'dan template'e veri aktarılır
- Django template syntax güvenlidir ve XSS ataklarına karşı otomatik koruma sağlar

## Kaynaklar
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Template Language](https://docs.djangoproject.com/en/stable/ref/templates/language/)
- [Django Built-in Template Tags](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
