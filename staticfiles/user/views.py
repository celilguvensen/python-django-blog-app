
from django.shortcuts import render,redirect # redirect fonksiyonu ile html sayfanın ismi ile gidebiliyoruz(214)
from .forms import LoginForm, RegisterForm # Bu klasör youlundaki forms dosyasından RegisterForm import ettik(213), (216) LoginForn'u da import ettik

from django.contrib.auth.models import User #(214) aslında djangonun modelini kullanıyoruz
from django.contrib.auth import login ,authenticate,logout # (214) login fonksiyonuna oluşturduğumuz user'ı verdiğimizde login olmuş olacak (216) DB'de username ve pass doğrulama işlemini yapıyor(authenticate) 218 logut ekledik

from django.contrib import messages # (215)

# Ders 212
# Create your views here.

def register(request): # (212)
    form = RegisterForm(request.POST or None)  # Aslında bu POST request gelmezse(GET Request gelirse) boş bir form oluştur anlamına geliyor. if ile kontrol yapmamış oluyoruz(214)

    if form.is_valid():
        # forms.py'de dic() olarak döndüğümüz değerleri alıyoruz
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        newUser = User(username = username) 
        newUser.set_password(password)
        newUser.save() # newUser'ı DB'ye kayıt etmiş oldu
        messages.info(request, "Başarıyla Kayıt oldunuz...") # (215)
        login(request,newUser) # User'ımızı oluşturuduktan sonra otomatik olarak login olmasını sağladı
        return redirect("index")    

    
    context = {      # Eğer is_valid çalışmazsa ya da GET request yapılırsa(GET request'te zaten is_valid'e girmeyecek) None sayesinde boş formu return edeceğiz
        "form":form
    }
    return render(request,"register.html",context)


    """Aşağıdaki yöntem oldukça uzun olduğundan pratik yöntemi uygulayacağız Ders 214
    if request.method == "POST": # Method kontrolü yapıyoruz
        form = RegisterForm(request.POST) # Method'umuz POST ise formu request.POS'taki bilgiler ile doldurmamız gerekiyor (214)
        if form.is_valid():
            # forms.py'de dic() olarak döndüğümüz değerleri alıyoruz
            username = form.cleaned_data.get("username") 
            password = form.cleaned_data.get("password")

            
            newUser = User(username = username) 
            newUser.set_password(password)
            newUser.save() # newUser'ı DB'ye kayıt etmiş olduk

            login(request,newUser) # User'ımızı oluşturuduktan sonra otomatik olarak login olmasını sağladık

            return redirect("index")

        # Burada "is_valid'i geçemezsek register.html sayfasına render olsun"

        context ={
            "form" : form
        }
        return render(request,"register.html",context)


    else:
        form = RegisterForm() # Boş bir form oluşturduk
        context ={
            "form" : form
        }
        return render(request,"register.html",context)"""
    


def loginUser(request): # (212) 
    form = LoginForm(request.POST or None) # (216)
    context = {
        "form": form
    }
    
    if form.is_valid(): # Burada is_valid ile formumuzun doğru gelip gelmediğini kontrol edeceğiz 216
        username = form.cleaned_data.get("username") # aslında biz burada clean yapmadık fakat Form class'ının içindeki clean çalışacak (216) Fakat register'da biz yazdık override ettik
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password=password) # DB'ye sorgu atacak (216) eğer yoksa None döner.

        if user is None: # Eğer user değeri None ise (216)
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı") # Önceki derste info danger mesajı olarak yazmıştık.(Layout.html'de)
            return render(request,"login.html",context)
        #Eğer None değil ise;
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    # Eğer GET request yapıldıysa ya da is_valid girmediyse login sayfasına geri dönecek(216)
    return render(request,"login.html",context)
def logoutUser(request): # (212) (218)
    logout(request)  #(218) Logout'a sadece request değeri veriliyor
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("index")