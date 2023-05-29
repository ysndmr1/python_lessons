# FlightApi devami

env activate ettikten sonra runserver da eger python env yi bulamadi diye bir hata gelirse env,.env,db.sqlite,debug dosyalarini silip kurulumlari en bastan yapmak gerekebilir

```
- python -m venv env
- git bash=> source env/Scripts/Activate
- pip install -r requirements.txt
- pip freeze
- cat > .env (bir env dosyasi olusturur)
ENV=development
SECRET_KEY=asdfdsf5454654
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

```
