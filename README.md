# 🐍 Django Kullanıcılar App Dersi

<div align="center">

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**Django'da Template Kullanımı ve Temel Özellikler**

*Başlangıç Seviyesi | Türkçe | Uygulamalı Öğrenme*

</div>

---

## 📚 Bu Derste Neler Öğreneceğiz?

✅ Django projesi başlatma (startproject)  
✅ Sanal ortam oluşturma ve yönetme  
✅ Yeni bir Django app oluşturma  
✅ HTML sayfaları (template) hazırlama  
✅ Sayfalara veri gönderme  
✅ Listelerle çalışma (for döngüsü)  
✅ Koşullu durumlar (if-else)  
✅ Sayfa linkleri oluşturma  

---

## 🎬 Sıfırdan Django Projesi Başlatma

### 📦 Gereksinimler

Başlamadan önce bilgisayarınızda bunların olduğundan emin olun:

- ✅ Python 3.8 veya üzeri
- ✅ pip (Python paket yöneticisi)
- ✅ Bir kod editörü (VS Code önerilir)

### 1️⃣ Python Kontrolü

Terminal'i açın ve Python'un yüklü olup olmadığını kontrol edin:

```bash
python --version
# veya
python3 --version
```

**Çıktı şöyle olmalı:** `Python 3.11.0` (veya benzeri)

---

## 🌐 Sanal Ortam Oluşturma (Virtual Environment)

> 💡 **Sanal Ortam Nedir?** Her proje için ayrı bir Python ortamı oluşturur. Böylece projelerinizin paketleri birbirine karışmaz!

### Windows için:

```bash
# 1. Proje klasörünü oluştur
mkdir djangokurs
cd djangokurs

# 2. Sanal ortam oluştur
python -m venv sanalortam

# 3. Sanal ortamı aktifleştir
sanalortam\Scripts\activate
```

### Mac/Linux için:

```bash
# 1. Proje klasörünü oluştur
mkdir djangokurs
cd djangokurs

# 2. Sanal ortam oluştur
python3 -m venv sanalortam

# 3. Sanal ortamı aktifleştir
source sanalortam/bin/activate
```

**Başarılı olduysa** terminal başında `(sanalortam)` yazısını göreceksiniz:

```bash
(sanalortam) C:\Users\Kullanici\djangokurs>
```

---

## 📥 Django Kurulumu

Sanal ortam aktif iken Django'yu kurun:

```bash
# Django'nun en son versiyonunu kur
pip install django

# Kurulumu kontrol et
django-admin --version
```

**Çıktı:** `5.0` (veya benzer bir versiyon numarası)

> 💡 **İpucu:** Tüm paketleri görmek için `pip list` komutunu kullanabilirsiniz.

---

## 🚀 Django Projesi Oluşturma

### Projeyi Başlat

```bash
django-admin startproject eticaret
```

> 💡 **Ne yaptık?** `eticaret` adında yeni bir Django projesi oluşturduk!

### Oluşturulan Klasör Yapısı

```
djangokurs/
│
├── sanalortam/              # Sanal ortam klasörü
│
└── eticaret/                # 👈 Yeni projemiz
    ├── eticaret/            # Ana proje klasörü
    │   ├── __init__.py      # Python paketi işareti
    │   ├── settings.py      # ⚙️ Proje ayarları
    │   ├── urls.py          # 🔗 URL yönlendirmeleri
    │   ├── asgi.py          # ASGI yapılandırması
    │   └── wsgi.py          # WSGI yapılandırması
    │
    └── manage.py            # 🔧 Django yönetim komutları
```

### Proje Klasörüne Gir

```bash
cd eticaret
```

---

## ⚡ İlk Çalıştırma

### Geliştirme Sunucusunu Başlat

```bash
python manage.py runserver
```

**Başarılı olursa** şöyle bir çıktı göreceksiniz:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Tarayıcıda Test Et

Tarayıcınızı açın ve şu adrese gidin:

```
http://127.0.0.1:8000/
```

**Django roket sayfasını** görüyorsanız tebrikler! 🚀 Kurulum başarılı!

---

## 🗄️ Veritabanı Kurulumu

Django varsayılan olarak SQLite kullanır. İlk migration'ları yapalım:

```bash
# Sunucuyu durdurun (CTRL + C)

# Migration'ları oluştur
python manage.py migrate
```

**Çıktı:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

> 💡 **Ne yaptık?** Django'nun varsayılan tablolarını (kullanıcılar, oturumlar vb.) veritabanında oluşturduk.

---

## 👤 Admin Paneli İçin Süper Kullanıcı

```bash
python manage.py createsuperuser
```

Sırasıyla şunları soracak:

```
Username: admin
Email: admin@example.com
Password: ••••••••
Password (again): ••••••••
```

Şimdi sunucuyu tekrar başlatın:

```bash
python manage.py runserver
```

Admin paneline girin:

```
http://127.0.0.1:8000/admin/
```

Oluşturduğunuz kullanıcı adı ve şifre ile giriş yapın! 🎉

---

## 📊 Proje Başlatma Akış Şeması

```
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO PROJESİ BAŞLATMA                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Python Kurulu?  │
                    └──────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Sanal Ortam Oluştur │
                  │   python -m venv     │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │    Aktifleştir       │
                  │  activate / source   │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │   Django Kur         │
                  │  pip install django  │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Proje Oluştur       │
                  │  startproject        │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Migration Yap       │
                  │  python manage.py    │
                  │       migrate        │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │ Süper Kullanıcı      │
                  │  createsuperuser     │
                  └──────────────────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Sunucu Başlat       │
                  │    runserver         │
                  └──────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  🚀 HAZIR! 🎉   │
                    └──────────────────┘
```

---

## 🚀 Başlangıç: Yeni App Oluşturma

### 1️⃣ Adım: App Oluştur

Terminal'i açın ve şu komutu yazın:

```bash
python manage.py startapp kullanicilar
```

> 💡 **Ne yaptık?** Django'da her özellik için ayrı bir "app" (uygulama) oluşturuyoruz. Mesela kullanıcılar için bir app, ürünler için başka bir app.

### 2️⃣ Adım: App'i Kaydet

`settings.py` dosyasını açın ve `INSTALLED_APPS` listesine ekleyin:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... diğer uygulamalar
    'kullanicilar',  # 👈 Yeni app'imizi ekledik
]
```

> 💡 **Neden?** Django'nun bu app'i tanıması için kayıt etmemiz gerekiyor.

---

## 📁 Proje Yapısı Nasıl Olmalı?

İşte doğru klasör yapısı:

```
djangokurs/
│
├── eticaret/                    # Ana proje klasörü
│   ├── eticaret/
│   │   ├── settings.py          # Ayarlar burada
│   │   └── urls.py              # Ana URL'ler burada
│   │
│   └── kullanicilar/            # Yeni app'imiz
│       ├── templates/           # 👈 HTML sayfaları burada
│       │   └── kullanicilar/
│       │       └── liste.html
│       ├── views.py             # 👈 Sayfa fonksiyonları burada
│       └── urls.py              # 👈 Bu app'in URL'leri
│
└── sanalortam/                  # Sanal ortam (virtual environment)
```

---

## 🎨 Template (HTML Sayfası) Oluşturma

### 1️⃣ Klasör Yapısını Hazırla

1. `kullanicilar` klasörü içinde `templates` klasörü oluştur
2. `templates` içinde `kullanicilar` klasörü oluştur
3. İçine `liste.html` dosyası oluştur

### 2️⃣ HTML Sayfasını Yaz

`kullanicilar/templates/kullanicilar/liste.html`:

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kullanıcılar Listesi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 {
            color: #092E20;
        }
    </style>
</head>
<body>
    <h1>Kullanıcılar Sayfası</h1>
    <p>Hoş geldiniz!</p>
</body>
</html>
```

---

## 🔧 View (Sayfa Fonksiyonu) Oluşturma

`kullanicilar/views.py` dosyasını açın:

```python
from django.shortcuts import render

def kullanicilar_listesi(request):
    """
    Kullanıcılar listesi sayfasını gösterir
    """
    return render(request, 'kullanicilar/liste.html')
```

> 💡 **render() ne işe yarar?** HTML sayfasını kullanıcıya göstermek için kullanıyoruz.

---

## 🔗 URL (Sayfa Adresi) Tanımlama

### 1️⃣ App İçinde URL Tanımla

`kullanicilar/urls.py` dosyası oluşturun:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.kullanicilar_listesi, name='kullanicilar_listesi'),
]
```

### 2️⃣ Ana Projeye Bağla

`eticaret/urls.py` dosyasını açın:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kullanicilar/', include('kullanicilar.urls')),  # 👈 Ekle
]
```

> 💡 **Artık sayfamız hazır!** `http://127.0.0.1:8000/kullanicilar/` adresinden ulaşabilirsiniz.

---

## 📦 Sayfaya Veri Gönderme (Context)

### View'ı Güncelle

```python
def kullanicilar_listesi(request):
    # Gönderilecek verileri hazırla
    context = {
        'baslik': 'Kullanıcılar Listesi',
        'toplam_kullanici': 150,
        'site_adi': 'Django Kursu'
    }
    
    # Veriyi sayfaya gönder
    return render(request, 'kullanicilar/liste.html', context)
```

### HTML'de Veriyi Göster

```html
<h1>{{ baslik }}</h1>
<p>{{ site_adi }} - Toplam {{ toplam_kullanici }} kullanıcı</p>
```

> 💡 **{{ }}** içinde değişken adını yazarak veriyi gösteriyoruz!

---

## 🔄 For Döngüsü - Liste Gösterme

### Kullanıcı Listesi Gönder

```python
def kullanicilar_listesi(request):
    # Örnek kullanıcı listesi
    kullanicilar = [
        {'ad': 'Ahmet', 'soyad': 'Yılmaz', 'yas': 25},
        {'ad': 'Ayşe', 'soyad': 'Kaya', 'yas': 30},
        {'ad': 'Mehmet', 'soyad': 'Demir', 'yas': 28},
        {'ad': 'Zeynep', 'soyad': 'Şahin', 'yas': 22},
    ]
    
    context = {
        'kullanicilar': kullanicilar
    }
    
    return render(request, 'kullanicilar/liste.html', context)
```

### HTML'de Listeyi Göster

```html
<h2>Kullanıcılar</h2>

<table border="1">
    <tr>
        <th>Ad</th>
        <th>Soyad</th>
        <th>Yaş</th>
    </tr>
    
    {% for kullanici in kullanicilar %}
    <tr>
        <td>{{ kullanici.ad }}</td>
        <td>{{ kullanici.soyad }}</td>
        <td>{{ kullanici.yas }}</td>
    </tr>
    {% endfor %}
</table>
```

> 💡 **{% for %}** döngü başlatır, **{% endfor %}** döngüyü bitirir!

---

## ❓ If-Else - Koşullu Durumlar

### Örnek 1: Liste Boş mu Dolu mu?

```html
{% if kullanicilar %}
    <p>✅ Toplam {{ kullanicilar|length }} kullanıcı bulundu.</p>
    
    <ul>
    {% for kullanici in kullanicilar %}
        <li>{{ kullanici.ad }} {{ kullanici.soyad }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>❌ Henüz kullanıcı bulunmamaktadır.</p>
{% endif %}
```

### Örnek 2: Yaşa Göre Rozet Göster

```html
{% for kullanici in kullanicilar %}
    <div class="kullanici-kart">
        <h3>{{ kullanici.ad }} {{ kullanici.soyad }}</h3>
        
        {% if kullanici.yas >= 30 %}
            <span class="rozet kirmizi">🏆 Kıdemli</span>
        {% elif kullanici.yas >= 25 %}
            <span class="rozet mavi">⭐ Deneyimli</span>
        {% else %}
            <span class="rozet yesil">🌱 Genç</span>
        {% endif %}
    </div>
{% endfor %}
```

---

## 🔗 Sayfa Linkleri (URL Tag)

### Neden `name=""` Kullanırız?

```python
# urls.py
urlpatterns = [
    path('', views.kullanicilar_listesi, name='kullanicilar_listesi'),
    path('detay/', views.kullanici_detay, name='kullanici_detay'),
]
```

### HTML'de Link Oluştur

```html
<!-- ❌ YANLIŞ: Direkt adres yazmayın -->
<a href="/kullanicilar/">Kullanıcılar</a>

<!-- ✅ DOĞRU: name kullanın -->
<a href="{% url 'kullanicilar_listesi' %}">Kullanıcılar</a>
<a href="{% url 'kullanici_detay' %}">Detay</a>
```

> 💡 **Neden?** Adres değişirse sadece `urls.py`'yi güncellemeniz yeterli!

---

## 🎯 Django Template Tagleri Özeti

### 📝 En Çok Kullanılanlar

| Tag | Açıklama | Örnek |
|-----|----------|-------|
| `{{ değişken }}` | Değişken yazdır | `{{ kullanici.ad }}` |
| `{% for %}` | Döngü | `{% for item in liste %}` |
| `{% if %}` | Koşul | `{% if yas > 18 %}` |
| `{% url %}` | Link oluştur | `{% url 'anasayfa' %}` |
| `{% load static %}` | CSS/JS yükle | `{% load static %}` |

### 🔧 Filtreler (Filters)

```html
{{ metin|upper }}                 <!-- BÜYÜK HARF -->
{{ metin|lower }}                 <!-- küçük harf -->
{{ metin|title }}                 <!-- Her Kelime Büyük -->
{{ liste|length }}                <!-- Uzunluk -->
{{ tarih|date:"d/m/Y" }}         <!-- 25/01/2024 -->
{{ metin|truncatewords:5 }}      <!-- İlk 5 kelime -->
```

### 🎨 Örnek Kullanım

```html
<h1>{{ baslik|upper }}</h1>
<p>Toplam: {{ kullanicilar|length }} kişi</p>
<p>{{ aciklama|truncatewords:10 }}</p>
```

---

## 👤 Kullanıcı Kontrolü (Authentication)

### Giriş Yapmış mı Kontrol Et

```html
{% if user.is_authenticated %}
    <!-- Kullanıcı giriş yapmış -->
    <div class="hosgeldin">
        <p>Hoş geldin, {{ user.username }}! 👋</p>
        <a href="{% url 'logout' %}">Çıkış Yap</a>
    </div>
{% else %}
    <!-- Kullanıcı giriş yapmamış -->
    <div class="giris">
        <p>Lütfen giriş yapın 🔒</p>
        <a href="{% url 'login' %}">Giriş Yap</a>
        <a href="{% url 'register' %}">Kayıt Ol</a>
    </div>
{% endif %}
```

### Admin mi Kontrol Et

```html
{% if user.is_staff %}
    <a href="{% url 'admin:index' %}" class="admin-link">
        🛠️ Admin Paneli
    </a>
{% endif %}

{% if user.is_superuser %}
    <button class="ozel-buton">⚙️ Süper Kullanıcı İşlemleri</button>
{% endif %}
```

---

## 🎓 Pratik Yapalım!

### Görev 1: Ürün Listesi

Bir `urunler` app'i oluşturun ve şu özellikleri ekleyin:

```python
# views.py
def urun_listesi(request):
    urunler = [
        {'ad': 'Laptop', 'fiyat': 15000, 'stok': 5},
        {'ad': 'Mouse', 'fiyat': 150, 'stok': 20},
        {'ad': 'Klavye', 'fiyat': 500, 'stok': 0},
    ]
    
    context = {'urunler': urunler}
    return render(request, 'urunler/liste.html', context)
```

```html
<!-- liste.html -->
{% for urun in urunler %}
    <div class="urun-kart">
        <h3>{{ urun.ad }}</h3>
        <p>Fiyat: {{ urun.fiyat }} ₺</p>
        
        {% if urun.stok > 0 %}
            <span class="yesil">✅ Stokta var ({{ urun.stok }} adet)</span>
        {% else %}
            <span class="kirmizi">❌ Stokta yok</span>
        {% endif %}
    </div>
{% endfor %}
```

---

## 📖 Komutlar Cheat Sheet

### 🎬 Proje Başlatma

```bash
# Sanal ortam oluştur
python -m venv sanalortam                    # Windows
python3 -m venv sanalortam                   # Mac/Linux

# Sanal ortamı aktifleştir
sanalortam\Scripts\activate                  # Windows
source sanalortam/bin/activate               # Mac/Linux

# Sanal ortamı deaktif et
deactivate

# Django kur
pip install django

# Django versiyonunu kontrol et
django-admin --version
```

### 🚀 Proje ve App Yönetimi

```bash
# Yeni proje oluştur
django-admin startproject proje_adi

# Yeni app oluştur
python manage.py startapp app_adi

# Sunucuyu başlat
python manage.py runserver

# Farklı portta başlat
python manage.py runserver 8080
```

### 🗄️ Veritabanı İşlemleri

```bash
# Migration dosyaları oluştur
python manage.py makemigrations

# Migration'ları uygula
python manage.py migrate

# Hangi migration'lar var göster
python manage.py showmigrations

# Migration'ı geri al
python manage.py migrate app_adi 0001
```

### 👤 Kullanıcı İşlemleri

```bash
# Süper kullanıcı oluştur
python manage.py createsuperuser

# Şifre değiştir
python manage.py changepassword kullanici_adi
```

### 🔧 Diğer Yararlı Komutlar

```bash
# Python shell aç
python manage.py shell

# Tüm paketleri listele
pip list

# requirements.txt oluştur
pip freeze > requirements.txt

# requirements.txt'ten kur
pip install -r requirements.txt

# Django admin komutlarını gör
python manage.py help
```

---

## ⚠️ Önemli Hatırlatmalar

### ✅ Yapılması Gerekenler

- Template dosyaları **mutlaka** `templates/app_adi/` içinde olmalı
- URL'lerde `name` parametresi kullan
- Context dictionary ile veri gönder
- `{% csrf_token %}` form'larda unutma

### ❌ Yapılmaması Gerekenler

- Direkt HTML'de URL yazmayın (`/kullanicilar/` yerine `{% url %}` kullanın)
- Template klasörünü yanlış yere koymayın
- App'i `INSTALLED_APPS`'e eklemeyi unutmayın

---

## 🎯 Sonraki Adımlar

1. ✅ **Model** oluşturmayı öğren (veritabanı)
2. ✅ **Form** kullanmayı öğren (veri girişi)
3. ✅ **Static dosyalar** ile çalış (CSS, JS, resimler)
4. ✅ **User Authentication** ekle (kayıt, giriş, çıkış)

---

## 📚 Faydalı Kaynaklar

- 📘 [Django Resmi Dökümantasyon](https://docs.djangoproject.com/)
- 🎥 [Django Template Dili](https://docs.djangoproject.com/en/stable/ref/templates/language/)
- 🔧 [Built-in Template Tags](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
- 💡 [Django Girls Tutorial (Türkçe)](https://tutorial.djangogirls.org/tr/)

---

## 🤔 Sık Sorulan Sorular

### S: Sanal ortam neden gerekli?
**C:** Her proje için ayrı paket versiyonları kullanabilirsiniz. Bir projede Django 4.0, diğerinde Django 5.0 kullanabilirsiniz.

### S: 'django-admin' komutu çalışmıyor?
**C:** Django kurulu olmayabilir. `pip install django` komutunu çalıştırın ve sanal ortamın aktif olduğundan emin olun.

### S: Sunucu başlatılamıyor, port kullanımda diyor?
**C:** 8000 portu başka bir program tarafından kullanılıyor. `python manage.py runserver 8080` ile farklı port deneyin.

### S: manage.py bulunamadı hatası?
**C:** Proje klasörünün içinde olduğunuzdan emin olun: `cd eticaret`

### S: Template bulunamadı hatası alıyorum?
**C:** Klasör yapısını kontrol edin: `templates/app_adi/dosya.html`

### S: CSS/JS dosyalarım yüklenmiyor?
**C:** `{% load static %}` yazmayı unutmuş olabilirsiniz.

### S: URL'ler çalışmıyor?
**C:** `settings.py`'de `INSTALLED_APPS`'e app'inizi eklediniz mi?

### S: Context verisi görünmüyor?
**C:** Dictionary'deki anahtar (key) ile template'deki değişken adı aynı mı?

### S: Migration hatası alıyorum?
**C:** `python manage.py makemigrations` komutunu çalıştırdınız mı? Sonra `migrate` yapın.

---

<div align="center">

### 🌟 Başarılar Dilerim!

**Sorularınız için:** [huseyint428@gmail.com](mailto:huseyint428@gmail.com)

Made with ❤️ and ☕ by Hüseyin Tunç

![Django](https://img.shields.io/badge/Django-Template-092E20?style=flat-square&logo=django)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner-green?style=flat-square)
![Turkish](https://img.shields.io/badge/Language-Turkish-red?style=flat-square)

</div>
