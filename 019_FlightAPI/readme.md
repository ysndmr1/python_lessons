# Flight Api nin devami

- bir önceki ders klasörunu kopyaladik ve bu bir git gubdan cekilmis bir dosya gibi dusundugumuz icin env,.env,dbsqlite,debug.log dosyalarini siliyoruz

```py
# for virtual environment module
- python -m venv env
# to activate
- ./env/Scripts/activate
- Powershell=>.\env\Scripts\activate
- git bash=> source env/Scripts/Activate
- linux/mac => source env/bin/activate

- pip install -r requirements.txt
- echo ENV=development > .env
- echo SECRET_KEY=dadasdas >> .env ilkinde dosyayi olusturup 2.de icine ekleme yapiyoruz
- python manage.py migrate
# To create admin
- python manage.py createsuperuser
- python manage.py runserver
```
