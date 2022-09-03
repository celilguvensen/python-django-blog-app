from dataclasses import field
from pyexpat import model
from socket import fromshare
# Ders 220
from django import forms
from .models import Article # models.py'de oluşturduğumuz Article modelini ekliyoruz (220)
# class ArticleForm(forms.Form): Bu yöntem her zaman kullanışlı değil. Article Formunu Article ModelForm'da üreteceğiz (220)
#     pass

# Article Modeli ile ModelForm kullanarak form üretme (220)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # models.py'de oluşturduğumuz Article modelini tanımlıyoruz (220) Burada model ile formumuzu bağlıyoruz. Django bizim Article modelimizde hangi alanlar varsa ona göre oluşturacak
        fields = ["title","content"] # Aslında biz author, title, content ve created_date alanlarını oluşturmuştuk. Burada created_date auto oluşturacak. author ise login olan kullanıcıya göre alacağız. Bu nedenle sadece title ve content inputlarını verdik. 220

