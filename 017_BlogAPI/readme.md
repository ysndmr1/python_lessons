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
# gitignore from toptal
```

⁡⁣⁣⁢-Firstly add app and rest_framework package to INSTALLED_APP in settings.py⁡⁡

###### The command to be used to install a project that we pulled from the repo with the package/versions downloaded in the requirements ->

```py
- pip install -r requirements.txt ()
```

--------- drawsql -----------------

- drawsql sayasinda er diagram olusuturuyoruz https://drawsql.app/, veritabanini grafik olarak göruntuleyebildigimiz bir uygulama, diagrami olusturduktan sonra bize kodlari hangi sql databaseinden almak istersek ona göre baslangicda secim yapip giriyoruz
- django user adinda django yerlesik user sistemini kullanacagimiz icin tek bir id ile olusturuyoruz
- 2 tane tablomuz olacak django da modeller veri tabaninda tablo ya denk geliyor
- category tablosu olsuturuyoruz ve name varchar
- blog yazilarinin olacagi bir tablo daha olusturuyoruz blog yazilari icin title varchar , content text, created_date date,updated_date date, category_id integer, user_id integer
- tablolarimizi birbiriyle iliskilendirirken foreignKey ile many to one iliski kuracagiz (foreignKey 2 positional arguman alir biri modelin ismi digeri silmek icin) post tablosundaki user id yi django user daki id ile many to one bagliyoruz
- ayni sekilde post daki user id ile category deki id ile foreignkey olarak manytoone iliski kuruyoruz

--------- blog sayfasinda model olusturma ---------

- class base ile category modeli olusturuyoruz () model oldugunu belirtiyoruz
- category name icine yazilan verbose name , name field ine denk gelen isim icin class meta ise model deki degistirmek istedigimiz özellikler icin

⁡⁢⁢⁢class Category(models.Model):
name = models.CharField(verbose_name='Kategori Adı', max_length=64)⁡

    ⁡⁢⁢⁢class Meta:
        verbose_name = 'Blog Kategori'
        verbose_name_plural = 'Blog Kategoriler'

    def __str__(self):
        return self.name

        ⁡

-⁡⁢⁣⁢ post icin model olusturuyoruz, iliski kuracagimiz fieldlarin (burada category) yanina id diye yazmiyoruz cunku django arka planda id ekledigi icin buraya yazarsak 2 id ust uste gelmis oluyor many to one iliski oldugu icin category modeli foreignkey ve iliski kuracagimiz modelin adi ve silme islemini ekliyoruz⁡
-⁡⁢⁣⁣ delete cascade, category tablosunda bir silme islemi yapildiginda iliskilendirdigimiz tabloda da silme islemini yap demek⁡

- ⁡⁢⁣⁢post u user olusturdu seklinde user belirliyoruz fakat bir user birden fazla post olusturabilecegi icin many to one ve foreignkey yapiyoruz, djangonun yerlesik user modelinin adi User oldugu icin () icinde user modelini belirtecegiz ve import edecegiz (aramadan class User seklinde de nerede oldugunu bulabiliriz)⁡
- ⁡⁢⁣⁣modellerimize str yaziyoruz (str bize bir objeyi string olarak göruntulememizi saglar pythonda bir cok yerde kullanilabilir, django da admin panelinde modeli string olark göruntulememizi saglar)
- ⁡⁢⁣⁢modelleri bitirdikten sonra admin.py sayfasina gidip kullanmak istedigimiz modelleri ekliyoruz ve import ediyoruz
- admin panelinde kullanmak istedigimiz model icin ⁡
  ⁡⁢⁢⁢from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)
⁡

- ardindan makemigration, migrate yapiyoruz

- class meta, modelimizin icinde bir ic class dir ayrica modelimizde yapmak istedigimiz degisiklikler icin kullaniliyor

⁡⁢⁢⁢class Post(models.Model):
user = models.ForeignKey(
User, verbose_name='Kullanıcı', on_delete=models.CASCADE)
category = models.ForeignKey(
Category, verbose_name='Kategori', on_delete=models.CASCADE)
title = models.CharField(verbose_name='Başlık', max_length=64)
content = models.TextField(verbose_name='İçerik')
created_date = models.DateTimeField(
verbose_name='Oluşturulma T.', auto_now_add=True)
updated_date = models.DateTimeField(
verbose_name='Güncelleme T.', auto_now=True)

    class Meta:
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

    def __str__(self):
        # return self.category + ' / ' + self.title
        return f'{self.category} / {self.title}'

⁡

-------- FAKER --------

- fake verileri almak icin
- faker kullanmak icin server kapatiyoruz ve ⁡⁢⁣⁣pip install faker ardindan requirements⁡
- ⁡⁢⁣⁣blog altinda faker.py olusturuyoruz⁡
- ⁡⁢⁣⁣faker i ve kullanmak istedigimiz modelleri import ediyoruz⁡
- run fonk u yaziyoruz
- ⁡⁢⁣⁣bir instance olusturuyoruz ve faker modelinden istersek dil farkli dilde veriler olusturmasi icin dil belirtebiliyoruz⁡
- blog da kullanacagimiz categoryleri kendimiz belirliyoruz
- ⁡⁢⁣⁣yazdigimiz categories leri for döngusune aliyoruz⁡
- ⁡⁢⁣⁣new_category degiskenine category modelinin objelerine yeni bir category ekle ve ismi de for döngusunde yazdigimiz category olsun⁡
- ⁡⁢⁣⁣burada bir category listesi olusturduk ve 4 tane category ekledik ve bu categoryleri bir dönguye sokup 4 kategory e sirasi geldikce ekleme yapacak⁡
- ⁡⁢⁣⁣olusan categorylere post eklemek icin for in icinde her category de olmasini istedigimiz sayida range belirtiyoruz⁡
- post modeli objectlerine yeni bir post ekle, bu object in title, content iceriklerini gönderdik
- ⁡⁢⁣⁣category e de olsuturdugumuz new_category i ekledik yani yeni olusturulan post bu category e ait olacak⁡
- ⁡⁢⁣⁣user icinde user modelinin object inden ilkini getir seklinde yazdik ve User i import ediyoruz⁡

⁡⁢⁢⁢''' # https://faker.readthedocs.io/en/master/
$ pip install faker # install faker module
python manage.py flush # delete all exists data from db. dont forget: createsuperuser
python manage.py shell
from todo.faker import run
run()
exit()
'''

from faker import Faker
from .models import Category, Post
from django.contrib.auth.models import User

def run():
fake = Faker()
categories = ('Travel', 'Food', 'Sport', 'Economy')

    for category in categories:
        new_category = Category.objects.create(name=category)
        for _ in range(50):
            Post.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                category=new_category,
                user=User.objects.first()

            )

        print('Finished')⁡

- bu islemlerden sonra python manage.py shell yapiyoruz
- shell ortaminda blog modelinde olusturdugumuz faker daki run fonk nunu import ediyoruz ve run fonk calistiriyoruz ardindan fonk sonunda yazdigimiz finished komutunu gördukten sonra shell den cikiyoruz

--------- ⁡⁢⁣⁢blog klasöru icin serailizer⁡ -----------

- blog altinda serializer olusturuyoruz ve serailizer ve kullanacagimiz modellerimizi import ediyoruz
- category modeli icin serializer olusturuyoruz
- class meta ile iliskili oldugu modeli belirtiyoruz ve kullanmak istemedigimiz fieldlari belirtiyoruz

⁡⁢⁢⁢class CategorySerializer(serializers.ModelSerializer):
class Meta:
model = Category
exclude = []⁡

- post modeli icin serializer i yaziyoruz
- class meta ile modeli iliskilendiriyoruz ve görmek istemedigimiz field lari ekliyoruz
- ⁡⁢⁣⁢url sayfasindaki eklemden sonra api ara yuzunde yapcagimiz degisiklik⁡
- serializerda field tanimlama var burada user field ini bir daha tanimliyoruz user a stringrelatedfield diyoruz bu bagli oldugu category den ilgili veriyi al demek (yani user name i )
- bu islemden sonra user sayi degil de admin olarak degisti
- ayni islemi category icinde yapiyoruz (category ismi de geliyor)
- user ve category görduk fakat bize frontend de idleri de lazim olacak onun icin idlerini de ekliyoruz fakat idler integerField
- db de bunlarin iliskileri kurulmus sadece göstermemiz yeterli

⁡⁢⁢⁢class PostSerializer(serializers.ModelSerializer):
user = serializers.StringRelatedField()
user_id = serializers.IntegerField()

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Post
        exclude = [
            # 'created_date',
            # 'updated_date',
        ]⁡

------ ⁡⁢⁣⁢views.py da kullancagimiz view seti olusturma⁡ -----

- views.py da serializer da yazdigimiz modelleri veri serializer modellerini import ediyoruz (serializer da modelleri import ettigimiz icin burada tekrardan modelleri import etmemize gerek yok)
- kullancagimiz modelviewset i de import ediyoruz
- category icin modelviewser class i yaziyoruz ve queryset icinde category modeli object sinin tumunu al diyoruz ce serializer classi icinde category icin yazdigimiz serializer i yaziyoruz
- ayni sekilde post modeli icin viewset class ini yaziyoruz ve tanimlamalari yapiyoruz

⁡⁢⁢⁢from rest_framework.viewsets import ModelViewSet

from .serializers import (
Category, CategorySerializer,
Post, PostSerializer
)

class CategoryView(ModelViewSet):
queryset = Category.objects.all()
serializer_class = CategorySerializer

class PostView(ModelViewSet):
queryset = Post.objects.all()
serializer_class = PostSerializer⁡

---------- ⁡⁢⁣⁢url yapisi⁡ -----------

- main dosyasi altindaki urls.py a blog ile gelenleri blog.urls sayfasina yönlendir diyoruz msin altinda router icinde category ve post u ayri ayri yazmamak icin buraya gelen bir blog istegi uzerinden category ve post sayfalarinin yönlendirmesi icin router yapisini blog klasöru altindaki url de yapacagiz

⁡⁢⁢⁢urlpatterns = [
path('admin/', admin.site.urls),
path('user/', include('user.urls')),
path('blog/', include('blog.urls')),
]⁡

- blog altindaki urls.py dosyasina router yapisini kuruyoruz
- router ve kullancagimiz views lari import ediyoruz ve router a url uzantisi ve view lari ekliyoruz

⁡⁢⁢⁢from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.views import CategoryView, PostView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('post', PostView)

urlpatterns = router.urls⁡

- run server yaptigmizda postlari ve categoryleri göruntuleyebiliyoruz
- sayfayi actigimizda user i 1 olarak göruyoruz bu sekilde göruntulemek istenmiyor genelde normalde user i ismiyle görmek ve user id 1 seklinde görmek bunu degistirmek icin de serializer da degisiklik yapacagiz (serializer bölumune git)

--------- ⁡⁢⁣⁢Pagination⁡ -------------

- pagination yapmak icin main > settings de > rest_framework de kodumuzu yaziyoruz

⁡⁢⁢⁢'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 20,⁡

------------ ⁡⁢⁣⁢User App⁡ -------------

- startapp ile user app olusturuyoruz
- settings de > installed app e ekliyoruz
- main > urls.py icine user i da ekliyoruz

⁡⁢⁢⁢urlpatterns = [
path('admin/', admin.site.urls),
path('user/', include('user.urls')),
path('blog/', include('blog.urls')),
]⁡

- user altinda admin ve serializer dosyalarini aciyoruz
- model , serializer , views , urls dosyalarini aciyoruz sirasiyla doldurmaya baslayacagiz
- user djangoda yerlesik bir model oldugu icin yeni model yazmayacagiz db den kontrol ettigimizde user in icinde neler oldugunu görebiliriz eger ek olarak (picture gibi) bir seyler koymak istersek modele ekleriz

-------- ⁡⁢⁣⁢User App > serializer⁡ -------

- bir user olusturmayi yaptik simdi bir user i guncelleme yada silme islemi ekliyecegiz (admin panelden zaten yapilabiliyor bu ekleme ile api servisi uzerinden yapacagiz)
- serializer ve user i import ediyoruz ve ardindan olusturmak istedigimiz serializer i class olarak yaziyoruz, model tabanli serializer oldugunu belirtip model olarak User i veriyoruz
- user i api da göruntuledigmiz de gelmesini istemediklerimiz exclude icine ekliyoruz
- ⁡⁢⁣⁢password hashlemek icin eklemeler yapiyoruz⁡
- yazdigimiz modelserializer a gittigimizde create ve update fonk lari var fakat 2 tane fonk yazmayacagiz
- ⁡⁢⁣⁣modelsrlzr sayfasinda validate fonk göruyoruz bu fonk gelen veriyi direk return yapmis bu fonk validate islemi arasina yeni bir sey gelirse kullanmak icin yazilmis override icin kullanabiliriz ayni zamanda validation islemi hem create hem update de kullaniliyor 2 fonk override etmemize gerek kalmiyor⁡
- def validate i yazdiktan sonra return icinde super ile orjinal halini calistir diyoruz
- ⁡⁢⁣⁣password u sifrelemek ve validationdan gecirecek 2 fonk import ediyoruz ⁡
- ⁡⁢⁣⁣validate fonk icindeki attrs icinde fieldlar var burada password degiskeni olsuturp attrsden gelen password u atiyoruz ve bu password u import ettigimiz validate fonk dan geciriyoruz ⁡
- ⁡⁢⁣⁣attrs bir dic onu guncellemek icin attrs.update icine bir dic yazip guncelle demis oluyoruz⁡
- ⁡⁢⁣⁣password u makepassword fonk dan gecir ve password attr guncelle diyoruz⁡

⁡⁢⁢⁢class UserSerializer(serializers.ModelSerializer):
class Meta:
model = User
exclude = [

# "password",

"date_joined",
"groups",
"user_permissions",
"last_login",
]

    def validate(self, attrs):
        # ? Dogrulama Fonksiyonu
        from django.contrib.auth.password_validation import validate_password
        from django.contrib.auth.hashers import make_password  # ? Şifreleme Fonksiyonu

        password = attrs["password"]  # ? Password al.
        validate_password(password)  # ? Validation'dan geçir
        # ? Password şifrele ve güncelle
        attrs.update({"password": make_password(password)})

        return super().validate(attrs)  # ? Orjinal metodu çalıştır⁡

---------- ⁡⁢⁣⁢user app > views⁡ ------------

- views sayfasinda restf den kullanacagimiz modelviewset import ediyoruz ve serializerde olusturdugumuz serializeri ve kullanacagimiz model i import ediyoruz
- userview classi ni yazip icine modelviewset i veriyoruz, queryset e user objectsinin hepsini serialier class a da yeni yazdigimiz user serializer ini yaziyoruz

⁡⁢⁢⁢from rest_framework.viewsets import ModelViewSet

from .serializers import (
User, UserSerializer
)

class UserView(ModelViewSet):
queryset = User.objects.all()
serializer_class = UserSerializer⁡

---------- ⁡⁢⁣⁢user app > url⁡ ------------

- rest f den router i import ediyoruz
- router i register yap ve urlye bir yazmadan gelinen sayfaya userview baksin seklinde ekliyoruz
- .views den userview i import ediyoruz
- url patterns i += li degilde path seklinde yaziyoruz eger '' bos gelirse router.urls baksin seklinde (include ile birlikte ve () ici string degil)

⁡⁢⁢⁢from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView
from rest_framework.authtoken.views import obtain_auth_token

# ----------------------------------------------------------------

# Logout function:

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def logout(request):
request.user.auth_token.delete() # Token Sil.
return Response({"message": 'User Logout: Token Deleted'})

# ----------------------------------------------------------------

router = DefaultRouter()
router.register('', UserView)

urlpatterns = [
path('', include(router.urls)),
path('login', obtain_auth_token),
path('logout', logout),
]⁡

- artik user a api servisi uzerinden de ulasabiliyoruz ve get,post,put,delete islemlerini yapabiliyoruz
- api ara yuzu uzerinden url sonuna/user/ ekleyerek user create edecegimiz sayfaya geliyoruz ve yeni bir kullanici olusturuyoruz
- ⁡⁢⁣⁣kullanici olusunca admin panelinden farkli olarak password un hash lenmedigini göruyoruz⁡
- admin panel de islem form uzerinden yapiliyor fakat api arayuzu uzerinden serializer ile yapiyoruz adminde sifremizi hashleyerek yaziliyor
- ayrica admin panelde validation icin gerekli sartlar varken api de olustururken 123456 yapabiliyoruz bunun da degismesi gerekiyor
- hem user create de hem update de sifreleme islemi yapmamiz gerekiyor
- serializer sayfasina ekleme yapiyoruz cunku serializer cunku sistem ile arayuz arasinda convert yapan yer
- serialzerdaki islemlerden sonra api ara yuzunde sifre update islemini hash li bir sekilde yaziyor

------------ ⁡⁢⁣⁢Token Authentication⁡ --------------

- aut islemleri icin settings.py sayfasina giriyoruz ve rf sayfasindan tokenauth sayfasina gidiyoruz
- ⁡⁢⁣⁢installed apps e 'rest_framework.authtoken', ekliyoruz sisteme token la girisi eklemis olduk ve db etkileyen bir takim durumlar old icin makemigrations ve migrate islemleri ni yapmamiz gerekiyor ⁡
- dökumandan devam ediyoruz rest_framework altina ⁡⁢⁢⁢'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],⁡ yapistiriyoruz aldigimiz örnekte based ve session var bunlari kullanmayacagimiz icin token ile degistiriyoruz bununla beraber sisteme giris yöntemi olarak token kullanacagimizi belirtmis oluyoruz
- runserverdan sonra admin panele gittigimizde token in geldiginiz göruyoruz
- suanda post lara geldigimizde butun postlar görunuyor sadece sisteme giris yapanlar erisebilmesi icin settings.py altinda rf e ⁡⁢⁢⁢'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],⁡ ekliyoruz ve permissiondan sonraki kismi sadece giris yapanlar yönetebilsin giris yapmayanlar okuyabilsin seklinde ekliyoruz ilk ekledigimizle sisteme token ile giris yap ikinci ekledigimizle ise giris yapanlar yönetebilsin digerleri sadece okuyabilsin demis oluyoruz
- admin panelinden girdigimizde postlarin altindaki degistirme özellikleri kalktigini göruyoruz suan da sedece postlari göruntuleyebiliyoruz giris yapacagimiz denemelri postmande yapiyoruz cunku api sistemine token verdik fakat arayuzde session kullaniyor
- bu islemden önce giris yöntemi belirlememiz gerekiyor login logout yapmamiz gerekiyor

----- ⁡⁢⁣⁢login logout⁡ ---------

- user dosyasi altindaki url yi aciyoruz
- djangonun rf un hazir giris fonk var onu ekliyoruz
- ⁡⁢⁢⁢from rest_framework.authtoken.views import obtain_auth_token⁡ import ediyoruz
- urlpatterns altina path icinde ⁡⁢⁢⁢path('login', obtain_auth_token),⁡ ekliyoruz
- logout icin hazir bir fonk yok onu yazacagiz
- login icin postmande deneme yapiyoruz
- post man e login icin olan url yi ekliyoruz normalde django da sonuna / ekliyoruz fakat bu islem icin kaldirdik, daha sonra postmande body ye username ve password u ekliyoruz post ettigimizde bize token dönuyor
- dönen token i headers altinda auth a token olarak ekliyoruz
- postman de auth u kladirip denedigimizde veriler gelmiyor
- l⁡⁢⁣⁢ogout olmak icin token in silinmesi yeterli bunun icin path e logout ekliyoruz url baglantisindan sonra fonk adini giriyoruz logout adinda bir fonk yazacagiz⁡
- ⁡⁢⁣⁢serializer log out yapiyoruz ve fonk icine request yazmayi unutmuyoruz⁡
- ⁡⁢⁣⁢fonk na requestdeki user icideki authtoken objesi var onu sil diyoruz silinidigine dair bir message dönduruyoruz⁡
- ⁡⁢⁣⁢göruntuleme icin apiview eklemeyi unutmuyoruz ve apiview i import ediyoruz⁡

⁡⁢⁢⁢# ----------------------------------------------------------------

# Logout function:

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def logout(request):
request.user.auth_token.delete() # Token Sil.
return Response({"message": 'User Logout: Token Deleted'})

# ----------------------------------------------------------------

- bir sonraki derste hazir bir modulle butun islemleri halledebilecegiz ⁡
