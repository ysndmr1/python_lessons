⁡⁢⁣⁢------ Authentication and Permission-------
⁡

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
-python manage.py startapp appName
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

- admin sayfasina girdigimizde olusturdugumuz kullanicilara yada superuser in cesitli yetkileri verebiliriz yada kaldirabiliriz
- kullanicilari bir gruba ekleyebiliyir grup uzerinden de cesitli yetkiler verebiliriz
- gruba ekledigimiz bir kisi herhangi bir yetki vermesek bile grubun yetkilerini alir
- bu özelliklerin hepsini djangonun admin icin olusturdugu arayuzden ulasabiliyoruz
- djangonun bize verdigi user tablosuna ekleme yapmak istedigimizde yeni bir tablo olusturup arada birebir iliski kurarak yapabiliriz
- yada istedigimiz eklemeyi user sayfasinin en altina bir attiribute olarak ekleyebiliriz
- permissionlari eklemek icin restframework sayfasindaki doc den aliyoruz https://www.django-rest-framework.org/api-guide/permissions/
-
