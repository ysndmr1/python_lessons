⁡⁢⁣⁢-----Django restframework-function based views------⁡

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

- app klasöru altindaki urls.py sayfasinda url pattern e ana sayfaya gelen isteklere home diye bir fonk baksin istedik ve home fonk nunu views.py altinda tanimliyoruz bunu ⁡⁢⁣⁢eger HttpResponse olarak gönderirsek bu protokolde veri gönderecek yani tarayiciya html-css formatinda veri gönderecek⁡ fakat biz burada tarayici kullanmayacagiz api sistemi yazdigimiz icin ham veri uzerinden islem yapacagimiz icin burada ⁡⁢⁣⁢response kullanacagiz \*\*\*Response un özelligi objeyi json a ceviriyor icine python un obje verisi(dictionary) seklinde yazacagiz ve ⁡⁢⁣⁣Response u kullanabilmek icin resframeworkten import ediyoruz

- tarayicida veri görebilmek icin http protokolunde olmasi lazim⁡⁡ ama burada response kullaniyoruz http protokolu degil bu sekilde runserver yaptigimizda ⁡⁣⁢⁣assertion error veriyor bunu asabilmek icin django @api_view yazmis bunu kullanacagiz ⁡

- ⁡⁢⁣⁢@api_view hakkinda bilgi almak icin vscode arama cubuguna def api_view yaziyoruz (kucuk harfli oldugundan fonk oldugunu anliyoruz ) ve onun restframework decorators icinde oldugunu görduk ve oradan import ederek sayfamizda kullaniyoruz

- api_view sayesinde response u ekrana basabildik ⁡

  ⁡⁢⁢⁢@api_view()⁡
  ⁡⁢⁢⁢def home(request):
  return Response(
  {
  'message': 'Hello World'
  }
  )⁡

- ⁡⁢⁣⁣app altindaki url sayfamizda yazdigimiz fonk sayfasi olan views.py in icindeki kullancagimiz fonk import ediyoruz from .views import home gibi⁡

- yaptiklarimizi postman ile de test edebiliyoruz

- admin sayfasindaki db e ekledigimiz verileri api ortaminda göruntulemek istedigimizde (btn frameworkler bir model mantigi kullanir ve sistemler model uzerine kurulmustur ve model django ile bir obje yapisi ile konusuyor fakat biz bu model yapisini direk ekrana bastiramayiz frontend kismi json dan anlar bu aradaki json-->obje gecislerini serializer ile yapiyoruz ) serializer i baz alarak verilerimizi ekrana basacagiz

- fonk yazarak basliyoruz
- ⁡⁢⁣⁢butun ögrenci verisine ihtiyacim var bu yuzden modelin ismi model icindeki object in tamamini yaziyoruz⁡
- tabiki model sayfasindan student modelini import ediyoruz
- ⁡⁢⁣⁢aldigimiz model bir obje(queryset) bunu bir serializerden gecirecegiz serializer i tanimliyoruz ve app klasörumuz icinde kendi olusturdugumuz serializer.py dosyasi icinde olusturdugumuz converter imizi import ediyoruz ve tanimladigimiz serializer in karsinia yaziyoruz ⁡⁢⁣⁣ve bir önceki basamaktaki tanimladigimiz student object sini serializer icine yaziyoruz ve many i true yapiyoruz bu da birden fazla veri icerdigi anlamina geliyor⁡
- ⁡⁢⁣⁢bu satirda yazdigimiz code obje halindeki stundet i yazdigimiz Studentserilazerden gecirerek serializer degiskenine ata
- ⁡⁢⁣⁣ve atadigimiz bu veriyi Response ile ekrana yazdir diyoruz ⁡⁣⁢⁣fakat burada response u yazarken buraya kadar yazdigimiz verileri data icine attigi icin onuda response icinde serializer.data seklinde yaziyoruz
  ⁡
  ⁡⁢⁢⁢@api_view(['GET']) # Default: ['GET']
  def student_list(request):
  students = Student.objects.all()
  serializer = StudentSerializer(instance=students, many=True) # print(dir(serializer)) # print(serializer.data)
  return Response(serializer.data)⁡

- student_list olarak yazdigimiz bu fonk url sayfasinda cagiriyoruz ve views.py sayfasindan yapacagimiz importlari tuple veri olarak da yazabiliyoruz urlpatterns icinde de fonk lari cagiriyoruz

⁡⁢⁢⁢from .views import (
home,
student_list,
student_create,
student_detail,
student_update,
student_delete,
student_list_create,
student_detail_update_delete,
)

urlpatterns = [
path('', home),
path('student_list/', student_list),
path('student_create/', student_create),
path('student_detail/<int:pk>', student_detail),
path('student_update/<int:pk>', student_update),
path('student_delete/<int:pk>', student_delete),
path('student_list_create/', student_list_create),
path('student_detail_update_delete/<int:pk>', student_detail_update_delete),
]⁡

- ⁡⁢⁣⁢kayit olusturma islemi post ile yapiliyor kayit islemleri post ile guncelleme islemleri put ile yapiliyor

- create islemi ile bir veri olusturdugumuzda bunu yazdigimiz create fonk nuna gönderiyoruz gönderdigimiz bu verileri request ile aliyoruz api sayfasinda olusturulan veri bize gelirken request ile geliyor, serializer olusturarak basliyoruz ve requestden gelen datayi serializer a ceviriyoruz bir önce ki islemde objeyi json a cevirmistik burada json u objeye cevirecegiz
- eger gelen veri dogru ise bu veriyi kaydet basamagini yaziyoruz ve dogru oldugu durum icin bir status mesaji yaziyoruz ve status u de kullanmak icin rest_frmwrkden import ediyoruz
- ardindan else ile datanin false olma durumunu yaziyoruz

⁡⁢⁢⁢@api_view(['POST'])
def student_create(request):
serializer = StudentSerializer(data=request.data)
if serializer.is_valid():
serializer.save()
return Response({
"message": "Created Successfully"
}, status=status.HTTP_201_CREATED)
else:
return Response({
"message": "Data not validated",
"data": serializer.data
}, status=status.HTTP_400_BAD_REQUEST)⁡

---- istedigimiz tek bir kayidi get,post,put islemleri yapma----

- tek bir kayidi kullanacagimiz zaman id ye göre yapiyoruz ve urlsini yazarken sonuna id kismini ekliyoruz views de yazdigimiz fonk url sayfasinda hem import ediyoruz hem de url seklinde yaziyoruz
- guvenlik gerektirmeten islemleri get ile yapiyorduk bu fonk da get ile yaziyoruz ve request yanina pk parametresi de ekliyoruz tek bir veri cekecegimiz icin
- modelden cektigimiz veriyi bir degiskene atiyoruz ve get islemini id=pk e göre yapiyoruz
- olmayan bir id cagirdigimizda hata verecek ve bu hatayi duzenlemek icin , hata safyasi gelmesin fakat veri olmadigini belirtmesi icin get_object_or_404(Student, id=pk) seklinde yaziyoruz ve bu kullandigimiz
- aldigimiz ogje yi de okuyabilmek icin serializer ile json a ceviriyoruz ve fonk nu django short cut dan import ediyoruz
  ⁡⁢⁢⁢@api_view(['GET'])
  def student_detail(request, pk): # student = Student.objects.get(id=pk)
  student = get_object_or_404(Student, id=pk)
  serializer = StudentSerializer(instance=student)
  return Response(serializer.data)⁡

--- Tek bir veriyi guncelleme

- guncelleme icinde ayni sekilde pk ye ihtiyacimiz var ayni sekilde yaziyiruz ve bu islemi put islemi ile yaptigimizi belirtiyoruz
- önce gelen veriyi alacagimiz bir degisken yaziyoruz
- sonraki basamakta aldigimiz veriyi serializerden geciriyoruz fakat burada degistirecegimiz data verisini de ekliyoruz disardan gelen veri bize request ile geliyor , data=request.data
- sonra data dogru ise kaydet bilgisini döndur eger bilgi false ise ona göre message yayinla satirlarini yaziyoruz
  -views de yazdigimiz fonk urls.py sayfasinda import edip kullaniyoruz
  ⁡⁢⁢⁢@api_view(['PUT'])
  def student_update(request, pk):
  student = get_object_or_404(Student, id=pk)
  serializer = StudentSerializer(instance=student, data=request.data)
  if serializer.is_valid():
  serializer.save()
  return Response({
  "message": "Created Successfully"
  }, status=status.HTTP_202_ACCEPTED)
  else:
  return Response({
  "message": "Data not validated",
  "data": serializer.data
  }, status=status.HTTP_400_BAD_REQUEST)

⁡
--- tek veriyi silme ---

- silme islemini yine pk sini aldigimiz veriye göre yapacagiz ve islemimizin adi delete
- öncelikle silecegimiz veriyi aliyoruz
- sonra veriyi sil diyoruz
- islem icin bir message yaziyoruz

⁡⁢⁢⁢@api_view(['DELETE'])
def student_delete(request, pk):
student = get_object_or_404(Student, id=pk)
student.delete()
return Response({
"message": "Deleted Successfully"
}, status=status.HTTP_204_NO_CONTENT)⁡

----- Benzer fonksiyonlari birlestirme-----
----- Id gerektirmeyenler-------
-----kayit listeleme + yeni kayit -----

- benzer fonksiyonlari tek bir fonk altinda birlestiriyoruz, gelen request metoduna göre condition ekliyoruruz
- eger method get ise butun modeli getir bir serializerdan gecir ve bir response döndur diyoruz
- else yazmamizin sebebi baslanginca 2 method gelebilir diye belirttik eger get degilse post dur seklinde olacak fakat elif de yazilabilir
- post yapilirken bu sefer json olarak veri postlaniyor bunu serializerdan geciriyoruz ve gecerli ise kayit edip response dönduruyoruz
- son olarak da verilerin dogru bir sekilde gelmedigi durumu ekleyip hata kodunu ve message yaziyoruz
- views sayfasinda yaptigimiz degisiklikleri urls sayfasina import edip ekliyoruz

⁡⁢⁢⁢@api_view(['GET', 'POST'])
def student_list_create(request):
if request.method == 'GET':
students = Student.objects.all()
serializer = StudentSerializer(students, many=True)
return Response(serializer.data)
else:
serializer = StudentSerializer(data=request.data)
if serializer.is_valid():
serializer.save()
return Response({
"message": "Created Successfully"
}, status=status.HTTP_201_CREATED)
else:
return Response({
"message": "Data not validated",
"data": serializer.data
}, status=status.HTTP_400_BAD_REQUEST)⁡

--- id gerektirenler---
--- kayit göruntuleme, guncelleme,silme----

- yapacagimiz izlemleri api_view icinde tanimliyoruz
- islemleri yapacagimiz fonk adini veriyoruz
- yapacagimiz gelen metoda coklu if yapisi gibi olan match yapisini kullaniyoruz
- get yapacagimiz icin get de kullanacagimiz yapiyi aliyoruz gelen request seializer modelimizden geciriyoruz ve response dönduruyoruz
- sonra guncelleme metodumuz olan put icin yapiyoruz, request ile elimizde olan datayi serilzerdan geciriyoruz, data gecerli mi , gecerli ise kaydet ve degilse seklinde message lari ekliyoruz
- son olarak delete fonk nunu ekliyoruz
- hepsinde ortak olan student = get_object_or_404(Student, id=pk) satirini (modelden gelen verinin atama yapildigi satir) en uste ekliyoruz
- views e ekledigimiz fonk lari urls sayfasinda import edip kullaniyoruz

⁡⁢⁢⁢@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):

    student = get_object_or_404(Student, id=pk)

    match request.method:
        case 'GET':
            # Tek kayıt görüntüle:
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)

        case 'PUT':
            # Tek kayıt güncelle:
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully"
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    "message": "Data not validated",
                    "data": serializer.data
                }, status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            # Tek kayıt sil:
            student.delete()
            return Response({
                "message": "Deleted Successfully"
            }, status=status.HTTP_204_NO_CONTENT)⁡
