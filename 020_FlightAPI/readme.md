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
    updated_time = models.DateTimeField(auto_now=True)

    # -----------------------------------------------------------

# --------------------- Passenger ---------------------------

# -----------------------------------------------------------

class Passenger(FixModel):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('0', 'Prefer Not To Say'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS, default='0')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'⁡

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

    # --------------------- Flight ------------------------------

# -----------------------------------------------------------

class Flight(FixModel):

    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('SUN', 'Sun Airlines'),
        ('SEL', 'Selim Airlines'),
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

    def __str__(self):
        return f'{self.flight_number} # {self.airline}'

⁡

- sonraki model reservasyonlar (model isimlerinde cogul kullanmiyoruz)
- reservation ilk field i ucus erd den bakiyoruz
- bu class in model oldugunu belirtiyoruz
- flight in iliski tipi foreignkey ve iliski kuracagi model flight modeli yukarida yazdik delete durumunu da yaziyoruz
- diger iliski durumu da passenger bir ucusa birden fazla yolcu ekleyebilmek icin manytomany yapiyoruz(mtm olunca bir ucusa yolcu eklemek istedigimiz zaman yeni bir kayit olusturacak ) dersin devaminda sonrada foreignkey olarak degistirecegiz
- str icinde ucus ve [] icinde bu ucusta kac yolcu oldugu gösterilecek admin panelinde

⁡⁢⁢⁢# --------------------- Reservation -------------------------

# -----------------------------------------------------------

class Reservation(models.Model):
flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
passenger = models.ManyToManyField(Passenger)
created = models.ForeignKey(User, on_delete=models.CASCADE)
created_time = models.DateTimeField(auto_now_add=True)
updated_time = models.DateTimeField(auto_now=True)

# --------------------- Reservation -------------------------

# -----------------------------------------------------------

class Reservation(FixModel):
flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
passenger = models.ManyToManyField(Passenger)

    def __str__(self):
        return f'{self.flight} [{self.passenger.count()}]'⁡

- modellerin def **str** lerini yaziyoruz modele göre duzenlemesini yapiyoruz
- ⁡⁢⁣⁣modelleri yazdigimizda hepsinde de created,createdtime ve updated time oldugunu göruyoruz bunlara model standardi da diyebiliriz, bunlarin sayisi daha fazla da olabilirdi mesela uzerine ekleme yapmamiz gerekti tekrardan bu standardlari da yeni modele ekleyecek miyiz (bazen bu standardlar 10 taneden fazla olabiliyor) bunun icin fixmodel yazacagiz⁡
  -⁡⁢⁣⁣ standardlari bu fixmodel icine alacagiz bundan sonra yazacagimiz diger modellerde bu fix i kullanmak icin inherit edecegiz ve tekrardan yazmamiz gerekmeyecek⁡
- ⁡⁢⁣⁣2. fix model zaten bir model bunun icin cagirdigimiz model icinde tekrardan model oldugunu belirtmemize gerek yok sadece model adiyla cagirsak yeterli⁡
- simdiye kadar yazdigimiz modelleri fix modele göre bir daha guncelliyoruz

⁡⁢⁢⁢# --------------------- FixModel ----------------------------

# -----------------------------------------------------------

class FixModel(models.Model):
created = models.ForeignKey(User, on_delete=models.CASCADE)
created_time = models.DateTimeField(auto_now_add=True)
updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # dont create table.⁡

-⁡⁢⁣⁢ modeli bitirdikten makemigration ve migrate yapacagiz ve django bunlari db e bir tablo olarak atayacak fakat eger fix modelinin db e eklenmesini istemiyorsak class meta ile abstract ile modeli soyut tabloya dönusturme demis oluyoruz

------------- ⁡⁢⁣⁢Serializer⁡ -----------------

- import yaparak basliyoruz serializer i rf den
- modellerden de yazdigimiz modelleri import ediyoruz
- passenger icin serializer yaziyoruz baslangicta bunun bir serialzier old nu belirtiyoruz fakat sonrada fix ekleyince onunla degistiriyoruz fix de serializer old icin () bir daha serialzer diye belirtmemize gerek yok
- meta da baz aldigi model olarak passenger i yaziyoruz ve exclude u bos birakiyoruz
- f⁡⁢⁣⁢light da dep ve isim eklemesi yaptiktan sonra burada da aynisini gender icin yapiyoruz ve gender text ile serialzermodelfield i kullanip get ile göruntulemek istedigimiz degeri ekliyoruz ⁡

⁡⁢⁢⁢# --------------------- PassengerSerializer -----------------

# -----------------------------------------------------------

class PassengerSerializer(FixSerializer):

    gender_text = serializers.SerializerMethodField()

    class Meta:
        model = Passenger
        exclude = []

    def get_gender_text(self, obj):
        return obj.get_gender_display()⁡

- flight icin ser yazyoruz meta da baz aldigi modeli flight diyoruz
- verileri api arayuzunde göruntuledigimizde departure=1 göruyoruz fkat bunun ne oldugunu belirlemek icin flight serial ekleme yapiyoruz
- ⁡⁢⁣⁣yeni bir field ekliyoruz veriler icin de görunecek (departure_text) ve serializer a bunun icin bir metod olusturacagimizi söyluyoruz (serializers.SerializerMethodField()) onun degerini yazdir, o metod da get ile baslamali ve verdigimiz isimle ayni olmali (def get_departure_text(self, obj):)⁡
- ⁡⁢⁣⁢burada serializer a modelden bagimsiz bir field eklemis oluyoruz (göruntuleme amacli,göndermek zorunda oldugumuz bir deger degil) departure_text e bunun ciktisini methodfielddan alacak ve metodu da get ile tanimlamis olduk (departure 1 fakat departure text de sehir hangisi yazsin istiyorsak) modelde departure i choises olarak tanimladik bu django özelligi choices icin özel (sehir rakamini zaten göruyoruduk bunnla degerini de görmus olacagiz ) bunu da return obj.get_departure_display() ile yapiyoruz get ile departure u aliyoruz ve display ile göruntuluyoruz
- ayni mantigi arrival icinde yapiyoruz ⁡(departure da text ini biz öyle istedigimiz icin yaptik sadece rakam degil isim gözuksun istersek text olmadan yazabiliriz)
- baska bir sekilde ekleme icin ise exclude degil field kullanmamiz gerekiyor, ayni durumu havayolu sirket ismi görunsun icin yapmak istesek önce field icine görmek istedigimiz alanlari ekliyoruz ve sadece en alta get ile fieldname_display dersek direk choices daki ismi getirmis oluyoruz stringmetod a gerek kalmdi bu sekilde
- field ile exclude farkinda eger model e bir sey eklememiz gerekirse exclude da sadece modelde eklemek yeterli fakat field icin model e eklersek field a da eklememiz gerekiyor

⁡⁢⁢⁢# --------------------- FlightSerializer --------------------

# -----------------------------------------------------------

class FlightSerializer(FixSerializer):

    departure_text = serializers.SerializerMethodField() # return from get_field_name()
    arrival_text = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = (
            "id",
            "created",
            "created_id",
            "departure_text",
            "arrival_text",
            "created_time",
            "updated_time",
            "flight_number",
            "airline",
            "departure",
            "departure_date",
            "arrival",
            "arrival_date",
            "get_airline_display", # dont need SerializerMethodField.
        )

    # SerializerMethodField()
    def get_departure_text(self, obj):
        return obj.get_departure_display()

    # SerializerMethodField
    def get_arrival_text(self, obj):
        return obj.get_arrival_display()⁡

- reservation icinde yazdik ve baslangic icin meta yi yazip gectik diger özellikleri sonradan ekleyerek gidiyoruz
- pass ve flight a ekleme yaptiktan sonra reser a bakyoruz ve api arayuzunde flight da 1 görunuyor, fix ser da created id icin yaptigimizi burda flight icin yapiyoruz flight ve flight id ekliyoruz flight da
- reservation icin api arayuzunde passenger a baktigimizda coklu veri old göruyoruz 1,2 yaziyor fkat bilgiler yok bunun icin passenger i tanimliyoruz ve passengerSerializer veriyoruz (many=True old belirtiyoruz ) aynisini flight icin yazdigimizda reservation icin flight bilgilerinin de geldiginiz göruyoruz 1 numarali reservation göruntuledik ve bu bilgi altinda flight da passenger i da modellerde olusturudugumuz field leri ile birlikte göruntuluyor

⁡⁢⁢⁢# --------------------- ReservationSerializer ---------------

# -----------------------------------------------------------

class ReservationSerializer(FixSerializer):

    flight_id = serializers.IntegerField(write_only=True)
    passenger_ids = serializers.ListField(write_only=True)

    flight = FlightSerializer(read_only=True) # ForeingKey()
    passenger = PassengerSerializer(read_only=True, many=True) # ManyToMany()

    class Meta:
        model = Reservation
        exclude = []

    def create(self, validated_data):
        validated_data["passenger"] = validated_data.pop('passenger_ids')
        return super().create(validated_data)⁡

- model de fix tanimlamistik aynisini ser icinde yapacagiz
- baslangicta sadece adini yaziyoruz ve pass veriyoruz diger ser lari yazdikca fix i de degistirecegiz
- yazdigimiz seri () lerine fixSerializer yaziyoruz

⁡⁢⁢⁢# --------------------- FixSerializer -----------------------

# -----------------------------------------------------------

class FixSerializer(serializers.ModelSerializer):

    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)⁡

------------ ⁡⁢⁣⁢views⁡ -------------

- rf den kullanacagimiz viewmodel setini , serializer a yazdigimiz model ve serial lari da import ediyoruz
- fix mantigini burada da kullaniyoruz modelviewset ini yaziyoruz ve suanda ortak bir sey olmadigi icin pass yaziyoruz

⁡⁢⁢⁢# --------------------- FixView -----------------------------

# -----------------------------------------------------------

class FixView(ModelViewSet):
pass⁡

- passenger icin view yaziyoruz yazdigimiz fixviewden inherit ediyoruz
- queryset icin passengerdaki objelerin tumu ve kullanicagimiz serializer i da yaziyoruz
- aynilarini flight ve reservation icin de yaziyoruz

⁡⁢⁢⁢# --------------------- PassengerView -----------------------

# -----------------------------------------------------------

class PassengerView(FixView):
queryset = Passenger.objects.all()
serializer_class = PassengerSerializer

⁡⁢⁣⁢- ucuslar da yetkilendirme yapmak icin bu kisma ekleme yapiyoruz

- rf persmissindan isauth import ediyoruz ve herkes okuyabilir fakat sadece giris yapmis kisiler tarafindan olusturulabilir onun icinde permission_classes ekliyoruz ve liste [] icinde views in izinlerini ekliyoruz
- bir views a permission bu sekilde ekleniyor ⁡

⁡⁢⁢⁢# --------------------- FlightView --------------------------

# -----------------------------------------------------------

from rest_framework.permissions import IsAuthenticatedOrReadOnly
class FlightView(FixView):
queryset = Flight.objects.all()
serializer_class = FlightSerializer
permission_classes = [IsAuthenticatedOrReadOnly]

# -----------------------------------------------------------

# --------------------- ReservationView ---------------------

# -----------------------------------------------------------

class ReservationView(FixView):
queryset = Reservation.objects.all()
serializer_class = ReservationSerializer⁡

------ ⁡⁢⁣⁢url⁡ --------------

- router icin defrouter i import ediyoruz ardindan views larimizi import ediyoruz
- ve router icinde flightdan sonra url ye passenger isteklerine passengerview baksin ve digerleri de ayni sekilde olsun diye ekliyoruz

⁡⁢⁢⁢# '/flight/':
urlpatterns = [
]

# ---------- Router ----------

from rest_framework.routers import DefaultRouter
from .views import (
PassengerView,
FlightView,
ReservationView
)
router = DefaultRouter()
router.register('passenger', PassengerView)
router.register('flight', FlightView)
router.register('reservation', ReservationView)
urlpatterns += router.urls⁡

------------ ⁡⁢⁣⁢admin⁡ ------------

- admin sayfasina gelip kullanacagimiz modelleri import ediyoruz
- admin site da kullanacaklarimizi da ekliyoruz

⁡⁢⁢⁢from django.contrib import admin
from .models import (
Passenger,
Flight,
Reservation
)

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Reservation)⁡

- ardindan runserver yapip yaptiklarimizi kontrol ediyoruz
- /flight bizim yazdigimiz app ardindan birdaha /flight/ yazdigimizda view göruntuleniyor ve giris izni yok diyor cunku def olarak adminlere erisim izni verdik (if admin user) sisteme admin olugumuzu belirtmemiz gerekiyor admin panel de admin icin token olusturuyoruz
- token i modheader extensionunda request ekleyerek gönderiyoruz ve api arayuzunde erisim geldi
- diger url leri de denedigimizde calistiklarini göruyoruz
- yeni bir flight ekledigimizde bize kullanici soruyor admin panelinde(api arayuzunde ise created id gerekiyor) bunu otomatiklestirmek icin
- created id 3 modelde de vardi bunun icin serializer sayfasina gidiyoruz fixseri icine created id icin bu bir serializer dir ve integer kullan ve mecburi olarak isteme seklinde belirtiyoruz ve created icinde stringfield ekliyoruz kullanici adi su id si su seklinde db tablosunda görunuyor
- created id kullanici olusturuldugu zaman bir kere tanimlanacak o kadr degisiklik yapmak icin modelserializer icinde create fonk yazildigi yere gidip fonk override etmek icin kopyaliyoruz
- validated data icinde flightnumber,airline.... fieldlarinin hepsi var (validated date bir dic []) diyorum ki sen created id yi bana sorma bunu self.context ile giris yapmis user id den al
- bu sekilde created id göndermeden bir passenger fln eklerken bir kullaniciyi secmem gerekmeden halletmis olduk
- ve bunu fix de yaptigimiz icin digerleri icin de gecerli olacak

⁡⁢⁢⁢created = serializers.StringRelatedField()
created_id = serializers.IntegerField(required=False)

def create(self, validated_data):
validated_data['created_id'] = self.context['request'].user.id
return super().create(validated_data)⁡

- yazdiklarimizi kullanabilmek ve eksiklik var mi görmek icin admin panel uzerinden db e veri ekliyoruz passenger,flight vb
- views de permission yaptiktan sonra api arayuzunde kontrol ediyoruz ve ucus bilgileri geliyor fakar departure 1 seklinde bir bilgi var bu 1 nedir buna bakmak icin serializer a gidiyoruz
- serializer yaptigimiz eklemelerle flight da isimizi bitirmis olduk passenger a geciyoruz
- passenger a da eklemeleri yaptiktan sonra reservation a geciyoruz
