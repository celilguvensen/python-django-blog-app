from django.contrib import admin

# Register your models here.


# Ders 201 --> models.py'de oluştuduğumuz Article'ı burada kaydediyoruz

from .models import Article #.models bu klasördeki models'ten Article'ı al anlamına geliyor
# admin.site.register(Article) # admin.site.register fonksiyonu ile kaydediyoruz (201)  --> Bunu bir decorator gibi yazacağız(202)

# Biz bu app'ı önceki ders'te Django settings.py'de eklemedik. Şimdi onu ekleyeceğiz (201)

@admin.register(Article) # 201'de yaptığımız kayıt işlemini Decorator olarak yazıyoruz.Decorator her zaman fonksiyonlarda kullanılmıyor. Bazen class'larda da kullanılıyor (202)
class ArticleAdmin(admin.ModelAdmin): # Oluşturduğumuz ArticleAdmin admin içindeki ModelAdmin'den türeyecek (202)
    list_display = ["title","author","created_date"] # Sadece title bilgisi değil author bilgisi de gözükecek
     
    list_display_links = ["title","created_date"] # title ve created_date basıldığında article detay sayfasına gidilecek (202)
 
    search_fields = ["title"]  # search bar title adına göre arama yapacak (202)
 
    list_filter = ["created_date"] # Oluşturulma tarihine göre filtreleyebiliyoruz (202) Sadece tarih yazmayabiliriz. Diğer parametreler ile de bu işlemi yapabiliriz

    class Meta: # Meta ismini Django vermemizi söylüyor. Class içinde class yazıyoruz (202)
        model = Article  # Burada ArticleAdmin class'ı ile Article class'ını birleştirmiş oluyoruz (202)

