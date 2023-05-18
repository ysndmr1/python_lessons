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

- https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy sayfasindan default olani alip settings.py sayfasinda res_framework altina ekliyoruz, ⁡⁣⁣⁢bu kod satirinda isauthenticated var bunun kullanilabilmesi icin restfrmwrk sayfasindan authentication bölumune gidiyoruz https://www.django-rest-framework.org/api-guide/authentication/#api-reference
- bu sayfada 4 cesit auth metodu var burada beasic ve token i kullanacagiz ⁡
  ⁡⁢⁢⁢'DEFAULT_PERMISSION_CLASSES': [
  # 'rest_framework.permissions.IsAuthenticated',
  # ],⁡
- auth sayfsasindan ayni yere ekleyecegimiz basic auth kodu ile her giris de giris yapmak istedigimiz kisi icin sifre sorgusu olusturuyor

⁡⁢⁢⁢'DEFAULT_AUTHENTICATION_CLASSES': [

# 'rest_framework.authentication.BasicAuthentication',

# 'rest_framework.authentication.SessionAuthentication',

# ]

- burada yaptigimiz islemin benzerini views.py sayfasinda modelin altina ekleye⁡cegimiz auth classes ile de yapabiliriz, tuple yada list olarak yazilabilir ⁡⁢⁣⁣authentication_classes = [BasicAuthentication] ve kullanacagimiz auth metodunu import ediyoruz⁡ ⁡⁢⁣⁢fakat sifre sormayi kullanabilmek icin permission ile beraber kullanmamiz gerekiyor settings sayfasinda yaptigimiz gibi permission_classes = [IsAuthenticated] kodu aliyoruz ve gerekli importlarini yapiyoruz

- auth ve permission islemleri beraber kullaniliyor⁡, birbirlerinden bagimsiz degiller

---Token Auth ----

- restfrmwrk deki token auth sayfasina gidiyoruz ve settings altina ekleyerek basliyoruz
- ⁡⁢⁣⁢installed app e ekledikten sonra migrate yapmamiz lazim cunku bize saglayacagi token tablolarinin db e eklenmesi gerekiyor⁡
- todo ile auth islemlerini yaptigimiz app i ayiracagimiz icin user adinda bir app olusturduk
- bir app olusturdugumuzda settingsde installed app e ekliyoruz
- ⁡⁣⁣⁢yeni bir app de model olusturarak basliyoruz --> serializer olusturarak devam ediyoruz --> oradan views a --> daha sonra ise urls bu 4 ana islemi dönerek tekrar ediyoruz
- ⁡burada yapacagimiz islemde her olusuturulan yeni user da token olusmasini istiyoruz, token ve user iliskilendirilecek
- token olusturacagimiz fonk nu modele yaziyoruz ve bu fonk da signal kullanacagiz, signal kullanici olusturulduktan sonra bir signal olusutracak ve bunun adi post_save https://docs.djangoproject.com/en/4.2/ref/signals/
- fonk receiver ile yaziyoruz ve django.dispatch den import ediyoruz ve receive icine post save aliyor bunu da import ediyoruz, sender ile settings parametresi kullaniyoruz ve import ediyoruz django.conf den
- bu yaptiklarimizi restfrmwrk generating tokens sayfasindan da bulabilirz https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
- bu yazdiklarimizla artik her user da bir token olacak

⁡⁢⁡⁢⁢⁢from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token⁡

⁡⁢⁢⁢@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, \*\*kwargs):
if created:
Token.objects.create(user=instance)⁡

--Serializer--

- user icin serializer olusturmaya basliyoruz , serializer i import ediyoruz ve burada kullanacagimiz user modelini import ediyoruz
  from rest_framework import serializers
  from django.contrib.auth.models import User

- register islemi icin bir serializer class i yaziyoruz ve baslangic icin all yapiyoruz
- main deki url e gidip user icin url ekliyoruz daha sonra user altinda da bir url olusturuyoruz
- view sayfasini olusturuyoruz registration icin, sadece create edecegimiz icin create view kullansak yeterli, importlarini da yapiyoruz
  ⁡⁣⁢⁡⁢⁢⁢class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegistrationSerializer⁡⁡
- auth token bize log in , log out olusuturuyor ama register olusturmuyor o yuzden bu sayfada register i kendimiz olusturuyoruz
- sonrasinda url sayfasina gidip views da yazdigimiz modelemizi cagiriyoruz
  ⁡⁢⁢⁢from django.urls import path
  from .views import RegisterView

urlpatterns = [
path('register/', RegisterView.as_view())
]

⁡⁢⁣⁢- register icin serializer yazarken field kismina all demistik bunun icin register sayfasinda dolldurulmasi gerek bir cok alan cikti bunlari kendi istegimize göre sinirlandirmak icin fields i duzenliyoruz⁡ ⁡

⁡⁢⁢⁢class Meta:
model = User
fields = ['username', 'password', 'password2', 'email']⁡

- email i uniq olmasi ve password u de 2 kere yazmasi icin serializer i duzenliyecegiz
- UniqueValidator i import ediyoruz
  ⁡⁢⁢⁢email = serializers.EmailField(
  required=True,
  validators=[UniqueValidator(queryset=User.objects.all())]
  )

⁡⁢⁢⁣- password u 2 kere yazdiracagiz ve yazilan password u gizlemek istiyoruz ⁡⁡
⁡⁢⁢⁢password = serializers.CharField(
write_only=True,
required=True,
validators=[validate_password], # widgets = {forms.HiddenInput()}
)
⁡⁢⁢- 2.psswrd u yaziyoruz
⁡⁢⁢⁢password2 = serializers.CharField(
write_only=True,
required=True,
)

⁡⁢⁣⁢- django da default olarak gelen seyler var fakat 2 psswordun validate oldugunu kontrol default olarak yok onu da burada ekliyoruz
⁡
⁡⁢⁢⁢def validate(self, attrs):
if attrs['password'] != attrs['password2']:
raise serializers.ValidationError(
{'password': 'Password fields not matching!'})
return attrs⁡

⁡- sonrasinda create metodu yaziyoruz, bu metod yazdigimiz bu islemler ok se user i create edecek , eger bu islemi yapmazsak user hashlenmiyor
⁡⁢⁣⁢- burada user i create ediyoruz, User object sini aliyor username i olusturdugumuz username degiskenine validated_data parametresini kullanarak atiyor,ayni sekilde email icinde yapiyoruz, password u almiyoruz onu set ile hash leyerek alacagiz⁡

⁡⁢⁢⁢ def create(self, validated_data):
user = User.objects.create(
username=validated_data.get('username'),
email=validated_data.get('email'),
)
user.set_password(validated_data.get('password'))
user.save()

        return user

⁡

- kullanici register olduktan sonra login olacak ve burada token i kullaniciyla beraber frontend tarafina göndermemiz gerekiyor
- views a gidip create metodunu override ediyoruz
- serializer i tanimlayip token i kullaniciya ekleyecegiz
- serializer valid degilse bir hata mesaji döndur
- degilse user serializer i kaydet
- token olustur, Token i restfrmwrk den import ediyoruz, create ettigimiz user i tokendaki user a yaziyoruz
- token key ini response ile frontend e gönderecegiz, bunu yapabilmek icin data yi belirliyoruz, serializer a gelen data, o datanin icine tokeni koyuyoruz, onu da token in keyi ne atiyoruz
- burada override ettigimiz kisim createview icindeki create mixin de ki create fonk u
- kullandigimiz headers da oradan geliyor
- ⁡⁢⁣⁢token olusturma islemini burada yaptigimiz icin views icindeki token olusturmaya gerek kalmadi⁡
  ⁡⁢⁢⁢def create(self, request, \*args, \*\*kwargs):
  serializer = self.get_serializer(data=request.data)
  if not serializer.is_valid(raise_exception=False):
  return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
  user = serializer.save()
  token = Token.objects.create(
  user=user
  )
  data = serializer.data
  data['token'] = token.key
  headers = self.get_success_headers(serializer.data)
  return Response({'message': 'User created successfully!'}, status.HTTP_201_CREATED, headers=headers)⁡
