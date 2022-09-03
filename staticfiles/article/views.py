from django.shortcuts import render,HttpResponse,redirect,get_object_or_404 # HttpResponse göstermek için ekledik 204 # redirect ekledik 221 #  get_object_or_404 ekledik 224
from .forms import ArticleForm # addArticle fonksiyonunda article oluşaracağımız için Article Form'u ekliyoruz. 220
# Create your views here.

from django.contrib import messages # 221
from .models import Article

# Ders 204

def index(request): # Her view fonksiyonunda request değişkeninin ilk değer olarak bulunması gerekiyor
    #return HttpResponse("Anasayfa")
    context = {"numbers":[1,2,3,4,5,6,], "number1":10, "number2":20}
    return render(request,"index.html", context) # context ekledik. number key'ine 7 değerini verdik


def about(request):
    return render(request,"about.html") 


# Ders 210
# def detail(request,id):
#     return HttpResponse("Detail: "+ str(id))


# Ders 220

def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    #print(articles)
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):
    form = ArticleForm(request.POST or None) # 221
    if form.is_valid(): # Formumuzu check edeceğiz # 221
        article = form.save(commit=False) # 221
        article.author = request.user # 221
        article.save() # 221

        messages.success(request,"Makale Başarıyla Oluşturuldu...")
        return redirect("index")    

    return render(request,"addarticle.html", {"form":form})


def detail(request,id): # Burada article id'sini Django'dan otomatik olarak geliyor. 223
    # article = Article.objects.filter(id = id).first() # 223 dersinde yaptığımız işlemi commet line yaptık Çünkü get_object_or_404  fonksiyonu ile yazacağız
    article = get_object_or_404(Article,id = id) # Eğer id'li obje varsa gösterilecek yoksa 404 sayfası görüntülenecek # 224
    #print(article)
    return render(request,"detail.html",{"article":article})
