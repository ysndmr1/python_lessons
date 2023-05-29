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

------- ⁡⁢⁣⁢User application⁡ --------

- django-admin startapp user
- settings > base.py > installed app e yeni app i ekliyoruz
- core > urls.py > urlpatterns e user ekliyoruz, kullanici islmelerini user.url deki user app halletsin demis oluyoruz
  path('user/', include('user.urls')),
- user > urls.py dosyasi aciyoruz ve sirasiyla model,serializer, views,urls.py dosyalrini aciyoruz
- model sayfasinin icini bosaltiyoruz cunku djangonun yerlesik user sistemini kullanacagiz
  ----------- ⁡⁢⁣⁢Serializer.py⁡ -----------
- rf den serial ve user modelini import ediyoruz
- kullanacagimiz userserializer ini yazip model tabanli oldugunu belirtiyoruz
- baslangic icin meta altinda model olarak user i ve exclude [] seklinde yazdik
- bu baslangictan sonra views i yazmaya basliyoruz
- ⁡⁢⁣⁢kullanici olusturduktan sonra hashleme yapmak icin serializer icine validate fonk ekliyoruz⁡
- ⁡⁢⁣⁣bu fonk da create ve update yaparken django verileri bir validation dan geciriyor bu validationdan gecerken passwordumuzu hash le demis olduk, hem kontrol edip hem de sifrelemis oldu
- ⁡⁢⁣⁢kullaniciyi ait bir guncellemeyi password istemeden yaptirmak icin serializer⁡ a ekleme yapiyoruz; password validation islemi icin ekledigimiz validate fonk nuna bir if satiri ekliyoruz dic de get islemi yapmanin (veriyi almanin 2 yöntemi var biri [] ile cagirma yada get yazarak cagirma ) gelen attrs bilgisi icinde password de var oradan password u al ve false ekliyoruz ⁡
- ve password olmadan guncelleme yapabiliyoruz
- (class meta da exclude icine yazdigimiz bilgiler bize dönmesini istemedigimiz bilgiler oluyor)
- ⁡⁢⁣⁢ayni email ile birden fazla hesap acilabiliyor bunu degistirmek icin serializer icinde emailField i tekrardan tanimlamamiz gerekiyor ⁡
- email icin serializer icinde emailfiled oldugunu belirtiyoruz burada user icinde email var fakat mecburi degil biz bunu degistirmek icin tekrardan tanimliyoruz
- serializerdaki charfield icine geldigimizde email in de orada yazidigini ve required in none oldugunu göruyoruz onu da true ya ceviriyoruz
- rf icinde validator lar var env klasöru altinda package altinda restframework ordan da validators.py a geldigimizde django nun yerlesik validation fonk icinde kullanabilecegimiz bir sey olup olmadigina bakiyoruz ve unique validator a bakiyorz bu class ayni bilgiden bir daha olmamasini sagliyor bu validation u email icin kullanabiliriz
- öncelikle import ediyoruz
- ⁡⁢⁣⁣bunu nasil tanimliyacagimiza bakmak icin emailfield icine geliyoruz ve orada validators kullanildigini göruyoruz yani bizde validators i kullanabiliriz ⁡
- ⁡⁢⁣⁢validators da liste icinde [] unique validator i kullan diyoruz peki bu unique lik neye göre kiyasmayi nasil yapacak UniqueValidator a baktigimizda icinde bir queryset var oana göre tanimlama yapiyor bizde burada queryset verecegiz ki onun icinde bir kiyaslama yapacak queryset = kaydettigimiz maili al user object leri icindeki butun verileri al ve ayni olmamasina dikkat et diyoruz
- bu sekilde email zorunlu hale getirdik ve ayni email olmasin demis olduk ⁡
- api arayuzunde olan bir kullanici mailini baska bir kullanici icin yazdigimizda artik olmuyor
- ⁡⁢⁣⁣password icin de gönderdigimiz zaman guncellemesi göndermedigimiz zaman da bir degisiklik olmamasi icin serializer icinde passwordu de ayriyoruz⁡
- required kisminda false yaparak gerekli olmadigini belirtmis oluyoruz

⁡⁢⁢⁢email = serializers.EmailField(
required=True,
validators=[UniqueValidator(queryset=User.objects.all())]
)⁡

⁡⁢⁢⁢password = serializers.CharField(
required=False,
write_only=True,
)⁡

⁡⁢⁢⁢def validate(self, attrs):
if attrs.get('password', False):
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
password = attrs['password']
validate_password(password)
attrs.update({'password': make_password(password)})
return super().validate(attrs)⁡

--------- ⁡⁢⁣⁢views.py⁡ -------------

- rf den modelviewset import ediyoruz, serializerden kullanacagimiz modeli ve o model icin yazdigimiz serializer i da import ediyoruz ve baslangic olarak userview class i icinde modelviewset i yazip query set e user object sinin hepsini serializer_class icinde yazdigimiz serializer in adini veriyoruz

--------- ⁡⁢⁣⁢urls.py⁡ -------------

- router kullancagiz onun icin rf den defaultrouter import ediyoruz, view de yazdigimiz userview i de import ediyoruz
- kullanacagimiz default router icin degisken adimizi veriyoruz (router)
- register a bos gelen user istekleri icin userview baksin seklinde yazmis oluyoruz
- router yapisinin url sini de url pattern e ekle diyoruz
- standard bir router yapsi diger projelerde bu sekilde kullanilir

⁡⁢⁢⁢router = DefaultRouter()
router.register('create', UserCreateView) # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser
urlpatterns += router.urls⁡

- yerlesik bir model oldugu icin admin.py a eklemeye gerek yok
- api ara yuzunde user a gelip yeni bir kullanici ekleyerek test ediyoruz
- yeni user olusturdugumuzda passwordun hashlenmedigini görmus olduk bunu hashlemek icin serializer a eklme yapiyoruz

----------- ⁡⁢⁣⁢Token Auth⁡ -------------

- token sistemini aktif hale getirmek icin core > settings > base > installed app e ⁡⁢⁢⁢'rest_framework.authtoken',⁡ ekliyorz
- yine ayni yere ekliyoruz token kullancagimizi rest framework e de bildirmemiz gerekiyor django bir pyton modulu rf de bir django module u bu yuzden rf ye de giris yöntemi olarak token kullancagimizi bildiriyoruz (auth class yazan satir ile)

⁡⁢⁢⁢REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAdminUser'],
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 20,
}⁡

- rf dökmaninda geri dönduk bör önceki derste login logout islemleri icin login de hazir bir fonk kullanmistik logout icin de bir fonk eklemesi yapmistik bu islem icin hazir olan dj-rest-auth paketini kullancagiz onun dok sayfasina gidiyoruz

----- ⁡⁢⁣⁢dj-rest-auth⁡ -------

- pip install dj-rest-auth
- pip freeze > requirements.txt
- base de installed app e ⁡⁢⁢⁢'dj_rest_auth',⁡
- url sayfasina gidiyoruz ⁡⁢⁢⁢path('auth/', include('dj_rest_auth.urls'))⁡ url patterns altina ekliyoruz user dan sonra gelecek auth/ isteklerine bu paket baksin demis oluyoruz
- hem authtoken hemde restauth icin migrate yapmamiz gerekiyor
- bu paket bize user bilgilerini guncelleme, sifre degistirme ve unutma gibi durumlari da eklemis oldu
- normalde username ve password ile giris yapiyorduk fakat bu paket ile beraber email ve password ile giris yapabiliyoruz user/auth/login ile giris sayfasina gidebiliyoruz
- admin panele gidip user icin email ekliyoruz email ile girisi denemek icin
- postmande denedigimizde login post islemi ile token döndurmus oluyor bize
- postmande logout islemi icinde loginden bize dönen token ile cikis yapiyoruz
- kullanicinin tokeni ile postmande farkli islemler yapabiliyoruz guncelleme gbi user/auth/user/ yaptigimizda kullanici bilgilerini bize dönduruyor ve dönen veri ile ilgili guncelleme-degisim islemlerini put ile yapabiliyoruz dj-rest bize bu imkanlari sagliyor
- api arayuzunden yapmaya calistigimizda header göndermedigi icin yapamiyoruz extension kullanarak tarayici uzerinden de yapabiliyoruz
- Kullanici islemlerine dair olan butun islemleri suanda yapabiliyoruz
- ⁡⁢⁣⁣kullaniciyi ait bir guncellemeyi password istemeden yaptirmak icin serializer a gidiyoruz⁡(her guncelleme de kullanici sifresi hatirlamayalim yada girmeyelim diye )

--------- ⁡⁢⁣⁢Token Serializer⁡ --------

- serializer bize sadece token bilgisi gönderiyor hem token hem kullanici bilgileri gelsin 2 kere islem yapmak durumunda kalmayalim istiyoruz
- dj-rest-auth dökumanindan configuration icinde buluyoruz login islemini dj-rest yapiyor token icin de onun dökumanina bakmamiz gerekiyor
- ⁡⁢⁣⁢settings de rest_auth altinda bunu degistirebiliyoruz fakat yeni bir serializer yazmamiz gerekiyor fakat mevcut ayarlari da degistirmek istemiyoruz⁡
- serializer dosyasina geliyoruz ve önce kullanacagimiz ayari import ediyoruz
- bu ayarin icine gidip baktigimizda sadece key oldugunu göruyoruz ve biz user bilgilerini de eklemek istiyoruz
- ⁡⁢⁣⁢bunu icin yeni bir serializer yaziyoruz ve bu orjinal ayarlari aldigimiz TokenSerializer i oldugu gibi inherit ediyoruz gittigimiz ayarlar icinden class Meta yi da inherit ediyoruz meta icine de tokenSerializer icindeki meta yi da inherit et demis oluyoruz ⁡
- ⁡⁢⁣⁢ilk satirda yazdigimiz serializer de orjinali oldugu gibi al alt satirda da class metayi da al demis oluyoruz eger metayi almassak ayarlardaki model i de tanimlamamiz,import etmemiz gerekiyor gerekiyor⁡
- ⁡⁢⁣⁢metayi oldugu gibi aliyoruz ve fields a user ekle diyoruz ⁡
- ⁡⁢⁣⁣dj-rest in mevcut token nini override etmis oluyoruz
- ⁡ ⁡⁢⁣⁣swagger a gittigimizde tekrar execute dedigimizde token verisinin yaninda user id sininde geldigini göruyoruz id nin görunmemesi icin yukari da tanimladigim bir user serializer im vardi user bilgilerimi oradan al seklinde user ekliyoruz swagger de tekrar calistirdigimizda hem token verisinin hem user verilerinin geldigini göruyoruz ⁡

⁡⁢⁢⁢from dj_rest_auth.serializers import TokenSerializer
⁡
⁡⁢⁢⁢class UserTokenSerializer(TokenSerializer):

    user = UserSerializer()

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')⁡

- yaptigimiz degisiklikleri sisteme de bildirmemiz gerekiyor bunun icin core > settings > base > e dokumantasyondaki ayari kopyaliyoruz
- bunu yazarken '' icini user ve serializer i da yazdigimiz userserializer olarak degistiriyoruz

⁡⁢⁢⁢# DJ-REST-AUTH SETTINGS:
REST_AUTH = {
'TOKEN_SERIALIZER': 'user.serializers.UserTokenSerializer',
}⁡
