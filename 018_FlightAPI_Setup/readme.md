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
--------- ⁡⁢⁣⁢Canli ortam ile test ortamini ayirma⁡ --------------
⁡- ⁡⁢⁣⁢canli ortam ile test ortamimiz arasinda settings.py klasörumuzde degisikler olmasi lazim cunku kullanacagimiz debug toolbarini kullanicinin görmemesi gerekir⁡

- wsgi doyasina gittigimizde web server ilk olarak bu dosyaya bakar oraya geldigimizde de core icindeki settings e baktigini göruyoruz bizim settigs.py klasörumuz bir modul flight dosyamizda bir modul, ⁡⁢⁣⁢bir modulu package acabilmemiz icin icine init dosyayi(bos da olsa) atmamiz yeterli ⁡
- core icinde settings adinda bir klasör aciyoruz bu klasöru moduler bir yapiya cevirecegiz icine **init**.py dosyayi aciyoruz ve klasörumuz bir modul oluyor yani ⁡⁢⁣⁢wsgi da settings acildiginda artik bu settings klasöru ne gidecek ⁡
- settings.py dosyasini development olarak degistirip settings klasöru icine atiyoruz
- ⁡⁢⁣⁣c⁡⁡⁢⁣⁣ore altinda settings.py vardi fakat biz onu core altinda baska bir klasöre atip calistiracagiz o yuzden BASE_DIR in sonuna bir parent daha eklememiz gerekiyor ⁡
- development dosyasini kopyala yapistir ile 2 tane daha aciyoruz birine base digerine production adini veriyoruz ve development ve prod dosyalarinin icini siliyoruz
- butun kodlari base e tasidik fakat bazi ayarlarimiz dev bazi ayarlarimiz prod dosyalarindan gelsin istiyoruz, genel ayarlari base de birakacagiz
- artik ENV dosyamizi aciyoruz ce secret key icin config import unu yapiyoruz
- debug ve allowed host u alip dev ve prod kopyaliyoruz ve base dekini yoruma aliyoruz
- ⁡⁢⁣⁣dev ortaminda debug true olabilir ve allowed host hepsini alabilir fakat prod ortaminda false yapiyoruz ve allowed host u 127.0.0.1 olarak degisitiriyoruz ⁡
- ⁡⁢⁣⁣installed app de debug toolbari prod ortaminda göstermemek icin installed api debug \_toolbar ile birlikte dev ortamina kopyaliyoruz ve prod ortamina da ekleyip debug_toolbari siliyoruz ve 2 sayfayada from.base import \* ile gecerli ayarlari import ediyoruz ve basede debug_toolbari yoruma aliyoruz (installedapp ve middleware += ekliyoruz )⁡
- ayni ⁡⁢⁣⁣sekilde middleware ide 2 dosyaya kopyaliyoruz ve toolbar icin ekledigimiz satiri middlewarede dev dosyasi altian kesip yapistiriyoruz ve prod ortaminda debugg olmayacagi icin middleware bos birakiyoruz⁡ ve baseden aldiklarimizi kaldiriyoruz
- ⁡⁢⁣⁣database i de alip 2 sayfayada yapistiriyoruz burada dev ortaminda sqlite prod ortaminda posgresql calistir gibi degistirebiliriz bu sekilde database leri de ayiriyoruz⁡ ve base de yoruma aliyoruz
- auth password u de 2 sayfaya yapistiriyoruz ve dev ortaminda icini bosaltip prod ortaminda oldugu gibi birakiyoruz bu sekilde biz test ederken surekli giris islemi yapmak zorunda kalmayacagiz
- static url ayarlarina da media ekliyoruz
  STATIC_URL = 'static/'
  STATIC_ROOT = BASE_DIR / STATIC_URL
  MEDIA_URL = 'media/'
  MEDIA_ROOT = BASE_DIR / MEDIA_URL
- en alta koydugumuz debug ip yide dev ortamina koyuyoruz prod ortaminda olmayacak
- init dosyasinda her seferinde prod ve dev icin import ayarini degistirmemek icin bu sayfayi env klasörune göre degistiriyoruz ⁡⁢⁣⁢env dosyasina ENV=development⁡ ekliyoruz ve init dosyasina da

⁡⁢⁢⁢from decouple import config
ENVIRONMENT = config('ENV')

if ENVIRONMENT == 'development':
from .development import *
else:
from .production import *⁡

- kodunu ekliyoruz eger gelen ENV development ise dev sayfasini degilse prod sayfasini import et seklinde degisitiriyoruz
- env den prod ve dev olarak degistirerek girecegimiz ortami secebiliriz her giriste projeyi kapatip aciyoruz

--------------------- LOGGING -------------------------

- https://docs.djangoproject.com/en/4.0/topics/logging/#logging doc ayarlari kontrol et
- developmentin en altina loggoing kodunu yapistiriyoruz
- logging icin her hangi module ihtiyacimiz yok yerlesik oldugu icin sadece ayarlari belirtmemiz yeterli
- log isleminde sistemimize giren herkesin kaydini tutacagiz (log kullanicinin hareketleri) eger kullanici bir hata alirsa log kayitlarindan girdigi zamana bakarak da hatalari cözebiliriz
- ⁡⁢⁣⁣formatters altinda standard kisminda eger standard ayarlarda bir log kaydi istersem altina yazdigimiz format ayarlarinda log kaydi tutacak⁡
- ⁡⁢⁣⁣verbose diye bir sablon daha var orada da formatta belirttigimiz ayarlari sakla diyoruz⁡
- ⁡⁢⁣⁣alttaki handlers da yakalama isleminin oldugu yer handlers altinda console da gösterecegi formatter i ve level i ayarlayabiliyoruz hangi seviyede istersek o seviyede kaydi bize gösterecek⁡
- file da ise log kaydini bize dosyalamasini istiyoruz orada da seviyesini belirliyoruz
- burada bana gösterirken info seviyesinde göster fakat dosyalarken warning seviyesinde dosyala diyoruz
- ⁡⁢⁣⁣file kisminda ki filename tarih girilip tarih bilgisini datetime fonk cekip hergun icin bir log dosyasi tutulabilir diger turlu log dosyasi cok siser⁡
- ⁡⁢⁣⁣ayni kodlari prod sayfasina da atip bazi bilgileri kaldiracagiz (dev ortaminda ayri prod ortaminda ayri loglama yapiyoruz )⁡
- prod da bize standard format lazim degil kaldiriyoruz
- console da calismayacagimiz icin console kismini da kaldiriyoruz
- asagidaki default ayarlardan da console u siliyoruz ve defaultdaki level i de warning yapiyoruz
