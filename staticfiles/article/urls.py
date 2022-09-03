# blog altındaki urls.py'den alıp import ettik. Burada include biz import ettik (211)
from django.contrib import admin
from django.urls import path

from . import views # views ve urls dosyaları aynı path'de olduğu için . koyduk

# Oluşturmuş olduğumuz urls.py'mize isim veriyoruz. Bunun sebebi ise redirect işlemi yaptımızda bu uygulamamızın bu url'ine diyebilmek için (211)

app_name = "article" # Biz article ismi verdik

urlpatterns = [
    #path('create/',views.index, name="index"),
    #path('',views.index, name="index"),  # Bu şekilde yaparsak eğer "http://127.0.0.1:8000/articles/" sayfasına gitmiş olur (211) 
    path("dashboard/",views.dashboard,name="dashboard"), # Ders (220)
    path("addarticle/",views.addArticle,name="addarticle"),
    path("article/<int:id>",views.detail,name="detail"), # 223

] 