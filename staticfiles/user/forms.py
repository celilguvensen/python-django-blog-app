# Ders 213

from django import forms
from django.contrib.auth.models import User # 215 soru cevap'tan ekledim



class LoginForm(forms.Form): # (216)
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget= forms.PasswordInput) # "widget=forms.PasswordInput" ile text alanı gibi değil, şifreliğ gözükecek


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput) # "widget=forms.PasswordInput" ile text alanı gibi değil, şifreliğ gözükecek (213)
    confirm = forms.CharField(max_length=20,label="Parola Doğrula",widget=forms.PasswordInput)

    # Djangoda Password'u confirm edebilmek için "clean" fonksiyonunu yazmamız gerekiyor. Böylelikle confirm ettikten sonra password'u submit edeceğiz (213)
    # oluşturduğumuz değişkenleri clean fonksiyonu altında da oluşturacağız (213)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")


        if User.objects.filter(username__iexact=username).exists(): # 215 soru cevap'tan ekledim
            raise forms.ValidationError('Bu kullanıcı adı kullanılıyor...')


        if password and confirm and (password != confirm):# Bu satır, parola ve confirm alanı doldurulmuş mu ve birbirine eşit mi? (213)
             raise forms.ValidationError("Parolalar Eşleşmiyor") # forms'da bulunan ValidationError ile hata gösteriyoruz

        # Eğer if bloğundaki şartlar sağlanırsa aşağıdaki kodlar çalışacaktır. Burada dict() olarak döneceğiz
        else:

            values = {
                "username" : username,
                "password" : password
            }

            return values  # Daha sonra values dict() döneceğiz
