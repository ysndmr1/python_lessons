# DRF Class Based View

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

- Class based view olusturmak icin view sayfasinda classimizi yazarak basliyoruz ve class isminin icine kullanacagimiz view i yaziyoruz, göruntuleme islemlerini yapan class temelde APIView dir, apiview i kullanmak icin import ediyoruz
- APIView i arayip gidip baktigimiz da icinde hangi fonk yazilidigini görebiliriz
- APIView da hangi http metodunu kullanacaksak o isim de bir fonk yazacagiz, fonk yazarken request yaziyorduk fakat suanda bir class icindeki bir fonk nu kullaniyoruz bunlar birer metod, ⁡⁢⁣⁢metodlarda ilk parametreye request yazamiyoruz self yazmamiz gerekiyor, request i sonra ekliyoruz
- student modelini oldugu gibi alip student degiskenine atiyoruz ve modeli import ediyoruz ⁡
- sonra serializerdan gecirmek icin olusturdugumuz serializerden geciriyoruz ve serializer i da import ediyoruz, icinde bir cok data oldugu icin de many true diyoruz
- ve serializer icindeki json verilerini alip, disariya yazdirma metodu olan Response ile return yapiyoruz, responsu da rf den import ediyoruz

⁡⁢⁢⁢class StudentListCreate(APIView):

    # Listele (GET Method):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)

    # Yeni Kayıt (POST Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

- tanimladigimiz views i url de path tanimlayarak yolunu belirliyoruz, views dan import ediyoruz, ⁡⁢⁣⁢url path yapisi gidecegi url ismini verdikten sonra bir fonk calistirir biz burada class adini verirsek calistirmaz bu yuzden kullandigimiz class icinde as_view fonk var onu cagirmamiz gerekiyor ⁡

⁡⁢⁢⁢urlpatterns = [
path('student_list_create/', StudentListCreate.as_view()),

]

- ⁡yeni kayit eklerken ve listelerken bizim id=pk ye ihtiyacimiz olmadigi icin fonk based yapida ayni olanlari birlestirmistik burada da ayni class altinda yeni kayit olan post fonk nunu kullanabiliriz
- create islemi yaparken (post) requestle gelen datayi al Serializerdan gecirerek bir degiskene ata, eger gelen veri dogru ise dogrulamasini yaptiktan sonra kaydet ve retrun yap, status un importunu yap

⁡⁣⁢⁣--- Tek kayit icin get,put,delete---

⁡⁢⁣⁣- Tek kayit göruntuleme islemleri icin class imizi yazip APIView i caigiriyoruz

- get fonk icinde self, request disinda pk i de parametre olarak yaziyoruz
- get fonk göruntuleme icin yaziyoruz getirdigimiz modelin ismini ve id sini verdigimiz fonk kayidi bulamadigi zaman sistem hatasi vermiyecek bulamadim diyecek o yuzden get_object_or_404 fonk nu kullaniyoruz ve import ediyoruz
- aldigimiz ögrenci verisini serializerdan geciriyoruz (api servisinin anlayacagi dile ceviriyoruz)
- ve data yi response ve return et⁡
  ⁡
  -- put--
- put fonk yaziyoruz icinde self,request,pk var
- degistirmek istedigim ögrenciyi verisini getiriyorum
- sonra gelen veriyi serializerdan geciriyorum ve () icine student disinda birde guncellenmesini istedigimiz request ile gelen datayi ekliyorum
- eger gelen veri valid ise kaydet ve guncellenen yeni veriyi Response ile göruntule ve basarili olduguna dair status kodunu dön degilse hata kodunu dön

-- delete--

- delete fon yazip self,request,pk i yaziyoruz
- sectigimiz id li veriyi getir bir degiskene ata ve o veriyi sil
- return ederken Response icine data silindigi icin data yazmiyoruz fakat message yaziyoruz ve status kodunu ekliyoruz
  ⁡⁢⁢⁢class StudentDetailUpdateDelete(APIView):

      # Tek kayıt görüntüle:
      def get(self, request, pk):
          student = get_object_or_404(Student, id=pk)
          serializer = StudentSerializer(instance=student)
          return Response(serializer.data)

      # Tek kayıt güncelle:
      def put(self, request, pk):
          student = get_object_or_404(Student, id=pk)
          serializer = StudentSerializer(instance=student, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      # Tek kayıt sil:
      def delete(self, request, pk):
          student = get_object_or_404(Student, id=pk)
          student.delete()
          return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

- views sayfasinda isimizi bitirdikten sonra bu classlari url sayfasinda cagirip import ediyoruz⁡

-- Simdiye kadar yazdigimiz 2 classi da birlestirme--

- bir class tanimlayip get,post,put,delete islemlerini ayni class da yaziyoruz
- class ismine APIView class ini parametre olarak veriyoruz
- simdiye kadar yazdigimiz yerdeki post,put ve delete metodunu oldugu gibi alip bu class altina yapistiriyoruz
- burada dikkat etmemiz gereken 2 kere kullanilan get metodu hem pk ile hem pk siz
- pk alacagimiz ve almayacagimiz durumlar olacak bunun icin baslangicta pk=0 verip eger pk varsa yada else seklinde yukarida yazdigimiz pk li ve pksiz fonk lari yapistiriyoruz
- urls sayfasina import edip kullaniyoruz fakat burada ⁡⁢⁣⁢dikkat etmemiz gereken durum pk li olan icin bir url olmayan icin baska bir url yazmamiz gerekiyor
  ⁡

⁡⁢⁢⁢class StudentGPPD(APIView):

    def get(self, request, pk=0):
        if pk:
            # Tek kayıt görüntüle:
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        else:
            # Kayıtları listele:
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students, many=True)
            return Response(serializer.data)

    # Yeni Kayıt (POST Method)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Tek kayıt güncelle:
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Tek kayıt sil:
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)⁡

--- GENERIC APIVIEW----

# GenericAPIView

# https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview

# Mixins

# https://www.django-rest-framework.org/api-guide/generic-views/#mixins

- generic apiview mixin ler icin gerekli altyapiyi saglayan bir class
- mixinler ise biz mixin i inherit ettikten sonra burada yazdigimiz data cekme gönderme islemlerini kendisi bu metod lar sayesinde yapar
- bunun icin drf sayfasinda tanimlanmis olan listleme,göruntuleme,guncelleme ve silme mixinleri hakkinda bilgi bulunuyor
- bu genericapiview i kullanmak icin mixinleri import ediyoruz (env icindeki restframework altindaki mixin.py icinde bulunuyorlar)
- mixin i import ettikten sonra yazdigimiz generic classinin icinde kullanacagimiz mixinleri inherit ediyoruz ve sonuna altyapi olarak gerekli onak genericapi i da ekliyoruz
- queryset olarak olusturdugumuz model objesinin hepsini veriyoruz ve serializer olarak kullanacagimiz serializer i da tanimliyoruz

class StudentGenericListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
queryset = Student.objects.all()
serializer_class = StudentSerializer

    # Listeleme:
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Yeni Kayıt:
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
