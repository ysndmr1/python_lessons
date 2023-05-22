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
- url sayfasindaki eklemden sonra api ara yuzunde yapcagimiz degisiklik
- serializerda field tanimlama var burada user field ini bir daha tanimliyoruz user a stringrelatedfield diyoruz bu bagli oldugu category den ilgili veriyi al demek (yani user name i )
- bu islemden sonra user sayi degil de admin olarak degisti

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

------ ⁡⁢⁣⁢views.py da kullancagimiz view seti olurturma⁡ -----

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
- sayfayi actigimizda user i 1 olarak göruyoruz bu sekilde göruntulemek istenmiyor genelde normalde user i ismiyle görmek ve user id 1 seklinde görmek bunu degistirmek icin de serializer da degisiklik yapacagiz
