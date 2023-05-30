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

- flight icin django-admin startapp flight ile app i olusturuyoruz ve setting > base > installed app e flight ekliyoruz ve settings > urls > urlpatters e ⁡⁢⁢⁢path('flight/', include('flight.urls')),⁡ ekliyoruz
- flight dosyasina gidip urls ve serializer dosyalarini olusturuyoruz
- sirasilya models, serializer, views, urls ve admin(model tanimladiktan sonra admin i dolduracagiz ve isimiz bitecek) dosyalarini aciyoruz

--------- models.py --------

- erd dökumanina baktigimizda django nun yerlesik user sistemi var hemen onu cagirarak basliyoruz
- erd deki passengerdan basliyoruz
- ⁡⁢⁣⁣bir passenger modelimiz olacak bu bir modeldir seklinde belirtiyoruz, fname ve lname i veriyoruz, gender tanimlamasini disinda yukarida yapiyoruz,gender i da charfield aliyoruz fkat karakter uzunlugu bir cunku bir tane harf olacak ve default a belirtilmedi seklinde ekliyoruz, email ini de ekliyoruz, crtd id ekliyoruz(yani bunu kim olusturdu) fakat iliski kuracagimiz yapida da id var ise burada id eklemiyoruz foreignKey ekliyoruz cunku many to one ve iliski kurdugumuz model user modeli delete durumunda da sil, created time (yani olusturdugumuz andaki time i ekle ) bir de aynisindan updated icin de olusturuyoruz ve passenger bitti⁡

⁡⁢⁢⁢from django.contrib.auth.models import User

class Passenger(models.Model):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('0', 'Prefer Not To Say'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS, default='0')
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)⁡

- siradaki modelimiz ucuslar erd den bakiyoruz
- class olusturarak basliyoruz ve model oldugunu belirtiyoruz
- flightnumber ile basliyoruz bazen iclerinde harf oldugu icin charfield yapiyoruz
- sirketleri disariya ekliyoruz
- altsatira airlines olarak ekliyoruz ve 3 oldugunu belirtip choices diyoruz
- kalkis ve varis icin sehirleri de ekliyoruz (normal sartlarda bu bir tablo olur ve iliski kurulur)
- departure ekliyoruz field type olarak (intfield 2 karakterli sayilar icin buyuk alan old icin yazmiyoruz ) positivesmallinteger veriyoruz choices i da veriyoruz ve aynisini arrival icin de yapiyoruz
- dep ve arr icin tarihleri ekliyoruz ve datefield veriyoruz
- created lari yukarda yazdigimiz yerden kopyaliyoruz

# --------------------- Flight ---------------------------

# -----------------------------------------------------------

⁡⁢⁢⁢class Flight(models.Model):

    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('SUN', 'Sun Airlines'),
        ('SWD', 'Sweden Airlines'),
    )

    CITIES = (
        (1, 'Adana'),
        (6, 'Ankara'),
        (7, 'Antalya'),
        (9, 'Aydın'),
        (10, 'Balıkesir'),
        (16, 'Bursa'),
        (32, 'Isparta'),
        (34, 'Istanbul'),
        (35, 'Izmir'),
        (44, 'Malatya'),
        (52, 'Ordu'),
    )

    flight_number = models.CharField(max_length=64)
    airline = models.CharField(max_length=3, choices=AIRLINES)
    departure = models.PositiveSmallIntegerField(choices=CITIES)
    departure_date = models.DateField()
    arrival = models.PositiveSmallIntegerField(choices=CITIES)
    arrival_date = models.DateField()
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

⁡

- sonraki model reservasyonlar (model isimlerinde cogul kullanmiyoruz)
- reservation ilk field i ucus erd den bakiyoruz
- bu class in model oldugunu belirtiyoruz
- flight in iliski tipi foreignkey ve iliski kuracagi model flight modeli yukarida yazdik delete durumunu da yaziyoruz
- diger iliski durumu da passenger bir ucusa birden fazla yolcu ekleyebilmek icin manytomany yapiyoruz(mtm olunca bir ucusa yolcu eklemek istedigimiz zaman yeni bir kayit olusturacak )

# --------------------- Reservation -------------------------

# -----------------------------------------------------------

class Reservation(models.Model):
flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
passenger = models.ManyToManyField(Passenger)
created = models.ForeignKey(User, on_delete=models.CASCADE)
created_time = models.DateTimeField(auto_now_add=True)
updated_time = models.DateTimeField(auto_now=True)
