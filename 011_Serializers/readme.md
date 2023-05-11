env klasöru acmak icin virtual environment kurmak icin

# python -m venv env

for win activate

# source env/Scripts/Activate

for install django

# pip install django

restframework kurarken önce rest framework kurularak baslanabilir cunku rstfrmwrk kurmak python otomatik olarak kuruluyor

yuklenen paketleri kontrol etmek ve bunlari bir klasörde tutmak icin

# pip freeze

# pip freeze > requirements.txt

proje olusturmak icin ve nokta ile ekstra bir klasör altinda kurulmamasi icin

# django-admin startproject main .

to run the server

# python manage.py runserver

to createapp

# python manage.py startapp appname

⁡⁢⁣⁢kurdugumuz app in altinda urls.py dosyasi olusturacagiz, bir projede birden fazla app olusturulabilir hepsinin kontrolunu project dosyasindaki urls uzerinden yapilirsa kalabaliga neden olur bu yuzden her bir app in urls sini kendi klasöru altinda aciyoruz ve bu app silindiginde de proje calismaya devam edebilsin⁡

---

⁡⁢⁣⁢project dosyasi altinda secret key var ve bu key i githuba pushladigimiz dosylarin icinde bulunmamasi icin buradan ayiracagiz
.gitignore klasöru icine django icin ekledigimiz code larin icinde bu code var ve ayrica bir env klasöru icinde de tutacagiz bunun icin decouple install edecegiz⁡

# pip install python-decouple

bu uygulamayi yukledikten sonra settings icinde import etmemiz gerekiyor

# from decouple import config

ve secret key yerine key imizi alip config icinde yazacagiz

# SECRET_KEY = config('SECRET_KEY')

⁡⁢⁣⁢.env klasöru acip key i yapistiriyoruz bosluk ve tirnak olmamasina dikkat ediyoruz
ayrica problemli gözuken karakterleri cikartabilirz hatta artik kendi istedigimiz bir sifre de belirleyebiliriz #,) gibi env ye ekledikten sonra settings icinden key imizi siliyoruz⁡

# SECRET*KEY=a!k7hr6nj%ay(1\*%%nl(2ah*^76tfu3=o3!3ue$14@

⁡⁢⁣⁢gitignore icine env yazdik env sonuna / koyarsak klasör oldugunu algilar fakat koymazsak env olan hem dosya hem klasörleri ignore eder⁡

django tarafindan create edilmis default tablolar var bunlari göruntulemek icin

# python manage.py migrate

⁡⁢⁣⁢serializer i uzerine kuracagimiz modellere olusturmaya basliyoruz, olusturdugumuz app klasörunde model.py a gdip modellerimizi olusturuyoruz burada olusturacagimiz her class database de bir tablo olusturacak class imiza isim vererek model oldugunu belirtiyoruz ⁡

⁡⁢⁢⁢class Student(models.Model):
first_name = models.CharField(max_length=50)
last_name = models.CharField(max_length=50)
number = models.IntegerField()

ve bu objenin isminin nasil görunecegini belirtiyoruz string representation
def **str**(self):
return self.first_name + ' ' + self.last_name⁡

⁡⁢⁣⁢app imizi main dosyasindaki settings de installed_apps altina ekliyoruz ⁡

olusturdugumuz modeli database imize kaydetmek icin

# python manage.py makemigrations

bu kodu calistirdiktan sonra app klasöru altina migrations dosyasi oto. olark olusuyor

appyl yapmak icinde

# python manage.py migrate

bu kod calisinca databse imiz olan db.sqlite icine bu tabloyu ekliyor

⁡⁢⁣⁢olusturdugumuz tablolari admin panelinde görmek icin app klasöru altindadaki admin.py a register olarak ekliyoruz, alacagimiz modelin nereden oldgunu belirterek import ediyoruz ⁡
⁡⁢⁢⁢from .models import Student
admin.site.register(Student)⁡

olusturduklarimizi admin panelinde görmek icin superuser olusturuyoruz

# python manage.py createsuperuser

user ile server i acmak ve roketi görmek icin

# python manage.py runserver

⁡⁢⁣⁣api a giris yapmak icin ⁡

# pip install djangorestframework

# doc icin https://www.django-rest-framework.org/

⁡⁣⁣⁢python objelerinin api a gönderilebilmesi icin json olmasi gerekiyor, her dil farkli bir dil kullanabilir fakat web tarafinda hepsi json(javascript object notation) a döner bu döndurme islemini serializer yapar, cift tarafli olarak calisabilir json gelen veriyi de python objesine cevirebilir

eklenen paketleri kontrol etmek ve projeye eklemek icin pip freeze > requirements.txt yapmayi unutma

⁡app imizin altinda serializer.py dosyasi olusturuyoruz
⁡⁢⁣⁢dosya icinde serializer i import ediyoruz⁡
⁡⁣⁢⁣from rest_framework import serializers

⁡⁢⁣⁢classimizi tanimlarken classname+serializer ve () icine inherit ettigimiz yer⁡
⁡⁣⁢⁣class StudentSerializer(serializers.Serializer):
first_name = serializers.CharField(max_length=50)  
 last_name = serializers.CharField(max_length=50)
number = serializers.IntegerField()

⁡⁢⁣⁢bir proje baslandiginda öncelikle model olusturulur --> sonra serializer --> sonra view dosyasi --> sonra url dosyasi seklinde hazirlaniyor⁡

views.py i simdilik hazir kullaniyoruz devaminda ögrenecegiz

⁡⁢⁣⁢olusturdugumuz appleri db de ulasmak ve kullanmak icin main altinda url sayfasinda eklemelerini yapiyoruz, ⁡⁢⁣⁢path sonuna include ekliyoruz, url icinde de path ile appmizin adini yaziyoruz ve include icinde app adi ve urls seklinde ekliyoruz ⁡

⁡⁢⁢⁢from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('student_api/', include('student_api.urls')),
]⁡

include eden dosya app altindaki url yi include ediyor fakat henuz o klasör olusturmamistik onu olusturuyoruz, sonrasinda kullanmak istedigimiz sayfalari kaynagindan import ederek basliyoruz ve urlpatterns i olusturuyoruz

⁡⁢⁢⁢from django.urls import path
from .views import home, student_api

urlpatterns = [
path('', home),
path('students/', student_api),

]⁡

runserver yaptigimizda main altindaki urls calisacak ve oraya admin ve student_sayfalarini yazmistik yukarida

⁡⁢⁣⁢hazirladigimiz serializerin endpoint i ni hazirlayacagiz, serializer 3th prty app yazdiklarimizi kullanmak icin settings.py altidindaki app icine rest_framework olarak eklememiz gerekiyor⁡

yazdigimiz serializer da bir obje create yada update etmek icin 2 method yazmamiz gerekiyor bunlari doc sayfasindan alip kendi projemize göre degistiriyoruz

⁡⁢⁢⁢def create(self, validated_data):
return Student(\*\*validated_data)

     def update(self, instance, validated_data):
         instance.first_name = validated_data.get(
             'first_name', instance.first_name)
         instance.last_name = validated_data.get(
             'last_name', instance.last_name)
         instance.number = validated_data.get('number', instance.number)
         instance.save()
         return instance

burada update isleminde () icinde bizden giden veri ilk sirada kullanicidan gelicek olan veri 2. sirada olacak sekilde yaziyoruz ⁡

⁡⁢⁣⁢serializer tanimlarken fieldlarimizi tanimladik ve create ve update metodlari tanimladik bunlari yapmamak icin daha kolay bir metod olan modelserializer kullanacagiz

⁡⁢⁢⁢class StudentSerializer(serializers.ModelSerializer):
class Meta:
model = Student # fields = ['number', 'first_name', 'last_name'] # fields = '**all**'
exclude = ['id']

class i oldugu gibi kullanmak icin class meta ile tanimliyorz⁡⁡ ve hangi model oldugu ve hangi fieldlarda degisiklik yapacaksak onlari aliyoruz ve code da 3 farkli sekilde kullandik, modelin icini de istedigimiz siralamaya göre yazabiliriz, exclude ile gösterilecek datanin istemedigimiz kismini cikarabiliriz
