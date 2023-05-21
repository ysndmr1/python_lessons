--- Flight App---

# for django project setup

```py
# for virtual environment module
- python -m venv env
# to activate
- ./env/Scripts/activate
- Powershell=>.\env\Scripts\activate
- git bash=> source env/Scripts/Activate
- linux/mac => source env/bin/activate
# To install the rest framework -- this command will automatically install django as well
- pip install djangorestframework
# to collect the requirements in a folder
- pip freeze > requirements.txt
# To create project
- django-admin startproject main .
# To create app
- python manage.py startapp appName
# We need decouple for env file --Note that this command is a python decouple, not a django decouple.
- pip install python-decouple
# To create the env file in the terminal and set the secret key
# Don't forget to change the secret key to config under the main folder
- echo SECRET_KEY=asdasdasfasf > .env
# To create admin
- python manage.py createsuperuser
# To save the changes to the database
- python manage.py makemigrations
- python manage.py migrate
# to run the server
- python manage.py runserver
```

⁡⁣⁣⁢-Firstly add app and rest_framework package to INSTALLED_APP in settings.py⁡⁡

###### The command to be used to install a project that we pulled from the repo with the package/versions downloaded in the requirements ->

```py
- pip install -r requirements.txt ()
```

---SDLC Software development Life Cycle---

- Requirements Analysis -> BRD, SRS, FRD/FRS
-     BRD stands for Business Requirements Document
      SRS stands for Software Requirements Specification
      FRD stands for Functional Requirements Document
      FRS stands for Functional Requirements Specification
- Design
- Development
- Testing
- Maintenance

---Entity Relationship Diagram (ERD)----

- drawsql sayfasindan yeni diagram cizerek basliyoruz
- django_user, flight, passenger, reservation tablolari olacak, her tablo gerekli bilgileri ekliyoruz
- yolcu icin adi soyadi id disinda bu yolcu bilgilerini kim olusturdu ve kim guncelledi durumlarini da ekliyoruz
- drawsql tablolarinin ekran göruntsu klasöre eklendi

---

- project ve app i olusturuyoruz sonra settings.py da installed app altinda app ismini ve kullandigimiz 3rd party library leri ekliyoruz
- temel kurulum icin migrate ve superuserlari yapiyoruz

⁡⁢⁣⁢---- Swagger and Redock -----
⁡- disariya acik public api servislerinin bir dökumantasyonu olmak zorunda, cunku sistemle irtibata gececek programcinin ne yapacagini bilmesi lazim

- swagger test yapma ortami ve api dökumani swaggerda hem test yapabliriz hem de dökumantasyon olarak kullanabiliriz , redock api dökumani
- https://drf-yasg.readthedocs.io/en/stable/readme.html
- bu sayfadaki tek bir modulle hem dökumantasyon hem de swagger kismini halledebiliriz
- ⁡⁢⁣⁣kurulumu icin⁡
- pip install drf-yasg (modul indirdikten sonra pip freeze > requirements.txt)
- installed apps e ekliyoruz eger statickfiles varsa eklemeye gerek yok
- ⁡⁢⁢⁢INSTALLED_APPS = [
  ...
  'django.contrib.staticfiles', # required for serving swagger ui's css/js files
  'drf_yasg',
  ...
  ]

⁡⁢⁣⁣- ana klasördeki url sayfasina kodu ekliyoruz ve gerekli importlari yapiyoruz (re_path)
⁡- ...
⁡⁢⁢⁢from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
openapi.Info(
title="Snippets API",
default_version='v1',
description="Test description",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="contact@snippets.local"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=[permissions.AllowAny],
)

urlpatterns = [
re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
...
]⁡

- schema view icinde title i kendi uygulama adimizla degistiriyoruz defult v disindaki 4 basligi da yoruma aliyoruz ve public altindaki permission classes i da yoruma aliyoruz
- bu koddan sonra api ara yuzune swagger ve redoc gelmis oldu
- urlpatterns i += seklinde yaziyoruz

------------ ⁡⁢⁣⁢DEBUG⁡ ----------------
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

- ⁡⁢⁣⁣debug toolbar kurulumu icin⁡
- pip install django-debug-toolbar(modulden sonra requirements)
- install app de staticfile olmasini istiyoru onu kontrol ediyoruz, static_url istiyor onu da kontrol ediyoruz
- installed apps e debug_toolbar ekliyoruz
- url sayfasina path ini de ekliyoruz
  ⁡⁢⁢⁢path('**debug**/', include('debug_toolbar.urls')),
  -middleware e "debug_toolbar.middleware.DebugToolbarMiddleware", kodunu ekliyoruz ⁡
- bu debug modulu guvenlik icin hangi ip kullanmakla ilgili bize bir ip veriyor ve bu kodu da settings.py a ekliyoruz

⁡⁢⁢⁢INTERNAL_IPS = [
# ...
"127.0.0.1",
# ...
]

⁡
