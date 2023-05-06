python3 to python (run only once)

```
echo alias py='python3' >> ~/.bash_profile
echo alias python='python3' >> ~/.bash_profile
echo alias pip='pip3' >> ~/.bash_profile
echo alias py='python3' >> ~/.bash_profile
echo alias python='python3' >> ~/.bash_profile
echo alias pip='pip3' >> ~/.bash_profile
echo alias py='python3' >> ~/.zshrc
echo alias python='python3' >> ~/.zshrc
echo alias pip='pip3' >> ~/.zshrc
echo alias py='python3' >> ~/.zshrc
echo alias python='python3' >> ~/.zshrc
echo alias pip='pip3' >> ~/.zshrc
```

```py

    python --version

```

$ python --version
$ python -m venv env
$ source env/bin/activate

# Powershell=>.\env\Scripts\activate

# git bash=> source env/Scripts/Activate

# linux/mac => source env/bin/activate

# for env-close $ deactivate

#github icin gitignore io ya gir django sec kodu al kendi dosyanda env ile ayni hizada .gitignore dosyasi ac onun icine kopyala

# pip install module_name

# pip uninstall module_name

# pip list

# pip freeze

$ ------installation Django------

# pip install django

# pip freeze ile djnagonun env icinde kurulu olup olmadigini anlayabiliriz

# pip freeze > requirements.txt ile dosya icindeki modulleri dosya icinde gösteriyor

# pip install -r requirements.txt ile requirements dosyasini gönderdigimiz kisi bu sekilde acip kullanabilir

# django-admin --version

# django-admin startproject projectName -- temel ayarlarimizin bulundugu klasör

# django-admin startproject projectName . # bosluk noktada yazinca ayni dosyadan 2 tane olusturmuyor ve . ise o dosya icinde yenisini ac demek

# nokta koymaz iseniz nested yapı oluşur. bundan sonraki komutlarda manage.py dosyasından faydalanılacak. nested yapı olursa komutu da ona göre yazmak gerekir veya iç klasöre geçip orda komut yazmak gerekir. o yüzden derslerde her zaman . ile proje başlatılacak

# django-admin startapp appName

# --------------Run Django ---------------

$ python manage.py runserver -- django dosyasini bir server olarak calistirmaya basliyor

# kapatmak icin ctrl + C

# db migrate db aktif etmek icin

# python manage.py migrate --bu komutla hazır olarak gelen paketlerde bulunan modeller(tablolar) sqlite a aktarılmış oldu

# python manage.py createsuperuser -- admin panele giris icin olusuturuyoruz

# go to admin dashboard

# http://127.0.0.1:8000/admin

#! komutlar
#python -m venv env(virtual env kurduk)(bunu yapmamızın sebebi her projeye ait packageler var biz bunları globale yüklemek istemiyoruz ve bir de sürümlerin uyuşmama gibi bir sorun çıkarmaması için kullanılır)
#! env i aktif etmek için
#Powershell=> .\env\Scripts\activate

# bash=> source env/Scripts/Activate

# linux/mac => source env/bin/activate

#! env i kapatmak için yani deactivate etmek için

# deactivate

#! powershel yetki hatası için
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
#! django kurulumu
#pip install django
#! proje oluşturma(fscohort13 proje adı)

# django-admin startproject fscohort1

# django için gerekli dosyaları kurmak için proje oluşturduk

#! iç içe olmadan proje başlatma komutu eğer nokta koymadan yukaridaki gibi girersek projeyi iç içe klasör yapısıyla oluşturuyor

# django-admin startproject fscohort13 .

#! app oluşturma

# python manage.py startapp student

# (student appı oluşturduk)(bunu yaptıktan sonra proje dizinine gidip settings.py e girip installepappse appimizi tanıtmamız gerekiyor)

#! databasei ayağa kaldırma

# python manage.py migrate

# (djangoda hazır gelen tabloları database e işliyoruz)

#! admin panel için superuser oluşturma

# python manage.py createsuperuser

# ardından gelen ekranda username password bilgilerini gir, mail girmene gerek yok.

#! projeyi ayağa kaldırma (default port 8000)

# python manage.py runserver

#! projeyi ayağa kaldırma (port numarasını değiştirme. aynı anda iki proje çalıştırmak istersek ikincisini ayağa kaldırırken port numarası ile ayağa kaldırmak önemli)

# python manage.py runserver 8080

#! yüklü paketleri listeleme

# pip freeze ya da pip list

#! yüklenen paketleri requirements.txt ye yazdırma
#pip freeze > requirements.txt
#(yüklü paketleri txt dosyasına kaydettik)(bunu yapmamızın sebebi projeyi sunduğumuzda kullandığımız paketleri göstermesi için (package.json gibi))
#! requirements.txt de bulunan paketleri yükleme komutu
#pip install -r requirements.txt (requirements.txt dosyasını kullanarak paketleri yükledik)(bunu repodan bir proje indirdiğimizde paketleri yüklemek için kullanıyoruz)
