from django.db import models

# Create your models here.


# Ders 201

class Article(models.Model): # Tablo yapımızı class şeklinde oluşturmamız gerekiyor
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name="Yazar") # on_delete = models.CASCADEile user silinirse User'a ait olan article'larda silinecek. Kullanıcımızı(auther) Djangonun içindeki tablodan "auth.User" ile alıyoruz
    title = models.CharField(max_length=50,verbose_name="Başlık") # Title models'in içindeki CharField'dan oluşturuyoruz. max length 50 yaptık
    content = models.TextField(verbose_name="İçerik") # content için TextField kullanıyoruz
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi") # models.DateTimeField(auto_now_add=True) ile oluşturma tarihini vereceğiz

    def __str__(self): # (202)
        return self.title




# Burada Article oluşturduk. Şimdi Admin Panel'de göstereceğiz. Admin.py'de kaydedeceğiz

# Article class'ında oluşturduğumuz değerlerin sonuna verbose_name = "" yazarak admin panelde o isimle gözükecektir (202)

# def__str__(self): --> methodu ile article'lar artık title isimleri ile listelenecek
