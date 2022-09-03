
from django.shortcuts import render,redirect,HttpResponseRedirect 
from .forms import LoginForm, RegisterForm 

from django.contrib.auth.models import User 
from django.contrib.auth import login ,authenticate,logout 

from django.contrib import messages 


def userNotLogged(func):
    def _func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            
            messages.info(request,"Yeni Kullanıcı Oluşturmak için Çıkış Yapınız")
            return HttpResponseRedirect("/")
        
        return func(request, *args, **kwargs)
    return _func

@userNotLogged
def register(request): 
    form = RegisterForm(request.POST or None)  

    if form.is_valid():
        
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        newUser = User(username = username) 
        newUser.set_password(password)
        newUser.save() 
        messages.info(request, "Başarıyla Kayıt oldunuz...")
        login(request,newUser) 
        return redirect("index")    

    
    context = {      
        "form":form
    }
    return render(request,"register.html",context)


    

@userNotLogged
def loginUser(request): 
    form = LoginForm(request.POST or None) 
    context = {
        "form": form
    }
    
    if form.is_valid(): 
        username = form.cleaned_data.get("username") 
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password=password) 

        if user is None: 
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı") 
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız...")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context)


def logoutUser(request): # (212) (218)
    logout(request)  #(218) Logout'a sadece request değeri veriliyor
    messages.success(request,"Başarıyla Çıkış Yaptınız...")
    return redirect("index")





