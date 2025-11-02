from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    urunler=[
        {
            "urun_adi":"Monster Laptop",
            "aciklama":"Monster Abra A16.5 oyuncu bilgisayarı",
            "resimler":[
                "https://ustunpatent.com/wp-content/uploads/2022/07/7124VM7ZR1S.jpeg",
                        "https://storage-monsternotebook-tr.mncdn.com/monsternotebook-tr/UPLOAD/ambassador-lp/new-setup-img.png"
            ],
            "fiyat":51999.99
        },
        {
            "urun_adi":"Asus  Laptop",
            "aciklama":"Asus  A16.4 oyuncu bilgisayarı",
            "resimler":[
                "https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSRqXRdD1AIoQV6U7K026_zVynQmIqLweppMZVviLw_cwawxo6IPliA1b6sc9ScJ_qPEPpLkvAIXuu-yPejw3AInelB9_tE0pXDFkX1TeCpHc8-9q-gnr_C",
                        "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcR-ZGpY_ViS6OzZl4exPI1Vcnu9hGO_tRKIm6Xx-ZN0ooaW6wAW8-9d--9jloJDaK9fyZ2rFgFd4PUH8lEWON2M8fvI47Qh4w"],
            "fiyat":51109.99
        }
    ]

    return render(request,"eticaret/home.html",{
        "urunler":urunler
    })
def category(request,kategori_adi):
    return render(request,"eticaret/kategori.html",{
        "kategori":kategori_adi
    })
