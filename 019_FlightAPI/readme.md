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
- ⁡⁢⁣⁣bu fonk da create ve update yaparken django verileri bir validation dan geciriyor bu validationdan gecerken passwordumuzu hash le demis olduk, hem kontrol edip hem de sifrelemis oldu⁡

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

--------- urls.py -------------

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
