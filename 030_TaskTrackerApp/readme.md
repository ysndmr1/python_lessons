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

- bu projede api kullanmayacagimiz icin env ve aktivate den sonra pip install django yaptik, djangonun yerlesik form ve template ini kullancagiz
- project ve app i olusturup createsuperuser yapiyoruz
- settings e todo ekliyoruz
- settings icinde teplatese geliyoruz birazdan olusturacagimiz html dosyalarimizi template icinde saklayacagiz templates altindaki app_dirs true template klasörunu app in icinde arayayim mi demek oluyor (izin icin), bir ustteki dirs ise template klasöru baska nerede olabilir diyelim ki bir cok app imiz var fkat temamiz bir tane ise ortak tema icin ortak bir alana saklamamiz lazim ana klasörde template aciyoruz ve dirs icine harici bir yerde kullandigimizi belirtiyoruz BASE_DIR / 'templates/', yaziyoruz
- main url de yeni bir path icinde '' bos birakirsak ana dizindeki herseyi includes ile da todo yazarak hepsine bunun bakmasini söyluyoruz
- todo altinda urls ve forms dosyalarini olusturuyoruz (serializer gibi onun yerine form yaziyoruz) burada render devreye girecek.
- ayni sekilde siramala yapiyoruz model,form view ve url dosyalrini aciyoruz
- serializer objeyi json ceviriyordu json u da objeye ceviriyordu form da form datayi objeye objeyi form data ya cevirecek
