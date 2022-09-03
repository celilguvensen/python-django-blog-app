"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include  # article altındaki urls'i include edeceğimiz için ekledik (211)

# article/views içindeki index fonksiyonunu kök url'e tanıtacağız. Bu nedenle index fonksiyonunu import edeceğiz

# from article.views import index # 204 206'da burada views'ın hepsini alacağız
from article import views # article app'nin tüm views'ını import ettik.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('articles/', include("article.urls")), 
    path('user/', include("user.urls")), 
] 


#path('detail/<int:id>', views.detail,name="detail"), (210)