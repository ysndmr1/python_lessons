env klasöru acmak icin virtual environment kurmak icin

# python -m venv env

for win activate

# source/Scripts/activate

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

kurdugumuz app in altinda urls.py dosyasi olusturacagiz, bir projede birden fazla app olusturulabilir hepsinin kontrolunu project dosyasindaki urls uzerinden yapilirsa kalabaliga neden olur bu yuzden her bir app in urls sini kendi klasöru altinda aciyoruz ve bu app silindiginde de proje calismaya devam edebilsin

---

project dosyasi altinda secret key var ve bu key i githuba pushladigimiz dosylarin icinde bulunmamasi icin buradan ayiracagiz
.gitignore klasöru icine django icin ekledigimiz code larin icinde bu code var ve ayrica bir env klasöru icinde de tutacagiz bunun icin decouple install edecegiz

# pip install python-decouple

bu uygulamayi yukledikten sonra settings icinde import etmemiz gerekiyor

# from decouple import config

ve secret key yerine key imizi alip config icinde yazacagiz

# SECRET_KEY = config('SECRET_KEY')

.env klasöru acip key i yapistiriyoruz bosluk ve tirnak olmamasina dikkat ediyoruz
ayrica problemli gözuken karakterleri cikartabilirz hatta artik kendi istedigimiz bir sifre de belirleyebiliriz #,) gibi env ye ekledikten sonra settings icinden key imizi siliyoruz

# SECRET*KEY=a!k7hr6nj%ay(1\*%%nl(2ah*^76tfu3=o3!3ue$14@

gitignore icine env yazdik env sonuna / koyarsak klasör oldugunu algilar fakat koymazsak env olan hem dosya hem klasörleri ignore eder

django tarafindan create edilmis default tablolar var bunlari göruntulemek icin

# python manage.py migrate
