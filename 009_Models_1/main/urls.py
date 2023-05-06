"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse # httpresponse fonk icinde yazarken hata verdi bu yuzden import etmemiz gerekiyor 

def home(request):
    return HttpResponse('''
        <h1>
        Welcome To Home
        </h1>
        
    ''')

urlpatterns = [
    # path ('url/´path/', view_func(),'redirection_name'),
    # url yönlendirmelerini burdan yapiyoruz 
    # djangoda url sistemi bir fonk calistigi zaman bir request gönderir o yzuden yazilan fonk bir req mutlaka yazilmali 
    # yazdigimiz fonk cagiracak path i yaziyoruz
    path('', home), #path(url,func) seklinde calisiyor
    path('admin/', admin.site.urls),
    path('fscohort/',include('fscohort.urls')),
]
