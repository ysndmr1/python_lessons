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
- ⁡⁢⁣⁣ve atadigimiz bu veriyi Response ile ekrana yazdir diyoruz ⁡⁣⁢⁣fakat burada response u yazarken buraya kadar yazdigimiz verileri data icine attigi icin onuda response icinde serializer.data seklinde yaziyoruz⁡
  ⁡⁢⁢⁢@api_view(['GET']) # Default: ['GET']
  def student_list(request):
  students = Student.objects.all()
  serializer = StudentSerializer(instance=students, many=True) # print(dir(serializer)) # print(serializer.data)
  return Response(serializer.data)⁡
