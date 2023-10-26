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
```

⁡⁣⁣⁢-Firstly add app and rest_framework package to INSTALLED_APP in settings.py⁡⁡

###### The command to be used to install a project that we pulled from the repo with the package/versions downloaded in the requirements ->

```py
- pip install -r requirements.txt ()
```

- bu projede api kullanmayacagimiz icin env ve aktivate den sonra pip install django yaptik, djangonun yerlesik form ve template ini kullancagiz
- project ve app i olusturup createsuperuser yapiyoruz
- settings e todo ekliyoruz
- settings icinde teplatese geliyoruz birazdan olusturacagimiz html dosyalarimizi template icinde saklayacagiz templates altindaki app_dirs true template klasörunu app in icinde arayayim mi demek oluyor (izin icin), bir ustteki dirs ise template klasöru baska nerede olabilir diyelim ki bir cok app imiz var fkat temamiz bir tane ise ortak tema icin ortak bir alana saklamamiz lazim ana klasörde template aciyoruz ve dirs icine harici bir yerde kullandigimizi belirtiyoruz BASE_DIR / 'templates/', yaziyoruz
- main url de yeni bir path icinde '' bos birakirsak ana dizindeki herseyi includes ile da todo yazarak hepsine bunun bakmasini söyluyoruz
- todo altinda urls ve forms dosyalarini olusturuyoruz (serializer gibi onun yerine form yaziyoruz) burada render devreye girecek.
- ayni sekilde siramala yapiyoruz model,form view ve url dosyalrini aciyoruz
- serializer objeyi json ceviriyordu json u da objeye ceviriyordu form da form datayi objeye objeyi form data ya cevirecek

---------- ⁡⁢⁣⁢Models⁡ ------------

- bu yazdgimiz modelde bir baslik, aciklama ve durumu var durumu choices seklinde, önceligi olacakve olustulma guncellenme tarihleri var

⁡⁢⁢⁢from django.db import models

status_choices = [
('C', 'Completed'),
('P', 'Pending'),
]

priority_choices = [
(1, 'High'),
(2, 'Medium'),
(3, 'Low'),
]

class Todo(models.Model):
title = models.CharField(max_length=50)
description = models.TextField()
status = models.CharField(max_length=1, choices=status_choices, default='P')
priority = models.SmallIntegerField(choices=priority_choices, default=2)
created_date = models.DateTimeField(auto_now_add=True)
updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title⁡

--------- ⁡⁢⁣⁢Forms⁡ ------------

- form u importlayarak basliyoruz
- modelden todoyu da cagiriyoruz
- class icinde model tabanli form oldugunu belirtiyoruz
- class meta icinde model imizi de todo ve gösterilmeyecek seylerin de olmadigini belirtiyoruz

⁡⁢⁢⁢from django import forms

from .models import (
Todo
)

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = []⁡

------------- Views --------------

- hem model tabanli hemde class tabanli viewslari yazacagiz
- todo object lerinin tumunu al ve degiskene ata
- verileri template bir dictionary icinde gönderiyoruz ve context degiskeni kullaniyoruz fakat degistirmek bize kalmis
- todos key i icinde bir ustteki degiskene atadigimiz object imiz olan todos u aktar diyoruz yada hic bu kadarda yazmadan butun veriyi render la render in ilk parametresi request 2.parametre ise kullanmak istedigimiz html sablonu ve formdan todo modelve formunu import ediyoruz

⁡⁢⁢⁢from .forms import (
Todo, TodoForm
)

# ------------------------------------

# Function Based Views

# ------------------------------------

# List:

def todo_list(request):
return render(request, 'list.html', {
"todos": Todo.objects.all()
})⁡

-------- ⁡⁢⁣⁢Templates⁡ -----------

- temp icin todo app icine klasörunu aciyoruz
- normalde bir class yazip o class i baska bir class da inherit edip kullanabiliriz ve ilk class da yazdigimiz fonk digerinde de ayni isimle cagirip override edebiliriz temp de de ayni mantikla base olarak olusturdugumuz yapiyi extend ederek kullaniyoruz ve block ile de override islemini yapmis oluyoruz temp icin
- if for gibi islemler icin {%%} kullaniyoruz degisken cagirmak icinde {{}} kullaniyoruz
- temp klasöru altinda bir base html olusturuyoruz
- bir baslik koyuyoruz sayfaya ve bir block ekliyoruz adina container veriyoruz ve icini bos birakiyoruz cunku diger sayfalarda cagirip override edecegiz
- bootstrap cdn ayarlarini ve js ayarlarini ekliyoruz
- views da list html cagirmistik o dosyayi acip base i extend ediyoruz
- ⁡⁢⁣⁢arada admin py da todo model ini import ediyoruz ve admin site register ini yapiyoruz ve url yi de ekliyoruz url de kullanacagimiz views i import ediyoruz ve url baglantisini pattern icine yaziyoruz ardindan makemigrations ve migrate yapiyoruz⁡
- runserver yapip örnek data ekliyoruz
- base html bir style ekliyoruz
- list html icinde base de yazdigimiz block container i override etmek icin cagiriyoruz baslik veriyoruz list e yapistirdigimiz code da bir tablo olusturuluyor
- ⁡⁢⁣⁢for döngusu icinde views deki dict ile gelen todos verisini kullanabiliyoruz ve herbir todo yu bir satirda yaziyoruz todo icinde priority var modelden geliyor (cunku todos a attigimiz veriyi de modelden almistik object icindeki basliklar modeldeki basliklar ) textlere style verilmis get_priority_display ise choices bir veriyi (serializer dersinden) text olarak göruntulemek icin basina get sonuna display ekliyorduk⁡
- bir alt satirda title ve olusturulma tarihi
- bir alt da ise statusune göre p pending ise danger yazdir degilse succes yazdir denilmis
  en alta da link verilmis yeni ekleme link i de tepedeki baslik altina yeni ekle diye bir a tag i var /add var onu birazdan yazacagiz bu bizi yazacagimiz add url sine göturecek

- ⁡⁢⁣⁢views da add icin bir fonk yaziyoruz return rende icinde request ve html dosyamizin adi olacak (add html yi olusturup icinde extend ve block container i yaziyoruz ve istediklerimizi de block larin arasina yazarak override edecegiz ) bir form yazacagiz bu form icine butun inputlari textboxlari tek tek yazmayacagiz djangonun burayi doldurmasini istiyoruz bunun icinde buraya form verisinin gelmesi gerekiyor orayi da views icndeki add fonk nuna yazacagiz ve context ekliyoruz fakat context icinde gönderecegmiz form datasini almamiz lazim onuda forms.py da yazdigimiz todoformdan alacagiz o da zaten icinde model tododan aliyordu bunu almak icin fonk altinda form degiskenine todoform u atiyoruz ve yukarida import etmistik bu form degiskenini de context icinde form keyi ile ver diyoruz (context gönderdigimiz icin renderda context i yazmamiz gerekiyor ) ve yeni yazdigimiz sayfanin url sini eklemeyi unutmuyoruz url sayfasinda views da yazdigimiz funk da cagiriyoruz ⁡⁢⁣⁣bu yeni sayfada ekledigimiz form elementinin todo list e eklenmesi icin bir de submit e ihtiyaci var o da add.html sayfasinda form un altina ekliyoruz ⁡⁡
- yeni eklemenin todo ya eklenmesi icin submit yaptigimizda csrf token istiyor bunun sebebi bizim canli da kullandigimiz bir sitede veriler benzer tag ve title isimleri ile gönderilebilir bu token ile gelen verinin dogrulugu kontrol ediliyor bu yuzden add sayfasinda form altina csrf token ekliyoruz

- gönderdigimiz veriyi almak icin views deki add de devam ediyoruz disardan post ile gelen veriyi (serializer gibi) form a dönusturmemiz lazim fonk altinda form a atadigimiz todoForm un icine request post ile veri gelebilir yada none gelebilir diyoruz if ile form verisi gelmis ise is_valid metodu calissin valid ise de save edilsin diyoruz ve veriyi kaydettigi zaman message versin diye django.contrib den message import ediyoruz ve eger kaydetme islemi basarili ise message.succes ile istedigimiz messagi veriyoruz ve altina eger ekleme islemi basarili ise bizi todo sayfasina götur demek icin redirect ile gönderecegimiz yeri yaziyoruz burada dikkat etmemiz gereken nokta her zaman ayni urlden gelmeyebilir bunun icin url sayfasinada kullanacagimiz urlnin sonuna name ile isim ekliyoruz ve burada da redirect ile oradaki name e gönderiyoruz url degisse bile name i kullandigimiz icin bir degisiklik olmayacak

# Add:
⁡⁢⁢⁢def todo_add(request):
form = TodoForm(request.POST or None)
if form.is_valid():
form.save() # Message:
messages.success(request, 'Kaydedildi.') # If OK redirect:
return redirect('todo_list') # redirect('path_name')
context = {
"form": form
} # return render(request, 'add.html', context)
return render(request, 'add_update.html', context)⁡

- ekledigimiz messag i nasil göruntuleyecegiz
- djangoda message direk göruntuleme olarak gorunmuyor bir msg kutusu var oraya atiyor eger göruntule dersek onu göruntuleyip siliyor, msg i baska sayfada göruntuleyebilirz, ayni sekilde delete update islemleri icinde msg yayinlayacagiz bunlari eger base html e eklersek sistemin tumunde aktif olur
- update icin
- url deki pk yi fonk icinde req yaninda yakaliyoruz
- degistirmek istedigimiz kaydin ilk halini pk ile al
- ⁡⁢⁣⁢(serializer da data ve instance lar vardi data yeni kayit icin instance ise mevcut bir data icin) todo add deki requestpost data aslinda ilk parametre icinde data oldugu icin yazmamiza gerek olmuyor data sana verdigim veriler yeni veriler demek bunlari objeye cevir diyoruz instance ise verdigimiz veriler mevcut veriler yani objeye cevirilmis halleri bunlari da forma cevir diyoruz update isleminin ilk basmaginda kayitli veriyi aliyoruz onu todo degiskenine atiyoruz sonra form degiskeni olusturup instance bu todo yu atamis oluyoruz bu iki satir mevcut kaydi aldigimiz satir⁡
- req post yapildimi eger yapildiysa mevcut veriyi yeni veri ile degistir
- eger veriler dogru ise kaydet ve msg yayinla ve ana sayfaya dön diyoruz

# Update:

⁡⁢⁢⁢def todo_update(request, pk):
todo = Todo.objects.get(id=pk)
form = TodoForm(instance=todo)
if request.method== "POST":
form = TodoForm(data=request.POST, instance=todo)
if form.is_valid():
form.save()
messages.success(request, 'Güncellendi.')
return redirect("todo_list")
context = {
'form': form,
'todo': todo
} # return render(request, 'update.html', context)
return render(request, 'add_update.html', context)⁡

- html sayfasina geldigimizde ise add ve update ayni fakat bir farklari var add de baslik icinde add todo yazarken update de mevcut verinin basligi {{ }} icinde yaziyor baslik önemli degilse 2 sayfa da ayni sekilde kullanilabilir

- delete islemi icin update gibi bir sablon kullanilabilir fakat gerek yok
- silmek istedigimiz veriyi yine pk ile aliyoruz
- get komutu ile id veriyi bir degiskene atiyoruz sonra o degiskeni siliyoruz ve msg yayinliyoruz ve todolist sayfamiza yönlendirecegiz

⁡⁢⁢⁢# Delete:

def todo_delete(request, pk):
todo = Todo.objects.get(id=pk)
todo.delete()
messages.success(request, 'Silindi.') # No need template.
return redirect("todo_list")⁡

------- ⁡⁢⁣⁢views icin class based⁡ -------------

- django icinde yerlesik bir takim class lar var listeleme create vs icin model viewset gibi tek bir class yok bunun icin ayri ayri class viewlari tanimlamamiz gerekiyor
- todo list icin listview a inherit edip kullanacagiz
- listview e baktigimizda icinde mixin ve baselist view oldugunu göruyoruz base view da get metodu ile listeleme ve gösterme islemleri yapiyor bunlari degistirmek icin bu get metodunu override etmemiz gerekiyor
- urls sayfasinda yazdigimiz view i import edip kullanacagiz class view da dikkat etmemiz gereken template icinde model icinde (todo) klasörunu de bekliyor o yuzden model adina olusturacagimz temp icin klasör olusturuyoruz
- fon yazaraken veriyi atayacagimiz ismi biz seciyoruz todos olarak ve verileri sayfada göstermek icin html icinde for döngusune alirken bu todos ismi ile cagiriyoruz fkat view kullandigimizda böyle bir atama yapmadigimiz icin (arka planda view bu islemi yapiyor cunku ) verinin gelen ismini kullanmamiz lazim html sayfasinda ve bu isim de object_list for döngusunde kullanirken object_list ile kullanacagiz
- ayni sekilde detail,create,update ve delete view larini da yaziyoruz
- template name altinda isim degistirmek istersek yeni isim verebiliriz burada default olani kullanmak istedigimz icin yoruma aliyoruz ayrica yeni isim versek de okuma sekli olarak temp altinda model\_ seklinde olmasi gerekiyor
- view a ekledigimiz class lar icin urls de tanimlamalarini da yaziyoruz
- ekledigimiz url ler icin html dosyalarini da olusturuyoruz
- list icin object_list kullanmistik detail icin ise de if de kullanacagimiz yerde model ismini kucuk harflerle yazarak yapiyoruz
- detail baglanti seklinde göstermek icin html sayfasinda if den sonra gerekli yerine a tag i icinde detail/ {{}} icinde model id sini veriyoruz
- create islemi icin kullancagimiz temp name \_form seklinde bize todo_form olarak html aciyoruz ve url ye de ekliyoruz
- listeleme ve detail icin bir göruntuleme yaptik fakat create isleminde bir de form olacak create vies icin kullanacgimiz form_class = todoForm seklinde create view a ekliyoruz, views lara özel yönlendirme yapmak icin revesed_lazy fonk kullaniyoruz redirect yerine reversed icine kullanacagimiz tag ise succes_url
- fonk yazarken msg yayinlamistik class based icin post metodunu override edip msg yayinliyoruz
- update islemi icin de post kullanildigi icin onu da override etmek icin post fonk aliyoruz ve istedigimiz msg ekliyoruz
- views de yaptigimiz islemler icin url lerini de yaziyoruz
- todolari siralamak icin list view icinde get ordering var onu list view e id leri en son ekledigimiz basa gelmesi icin -id olarak ekliyoruz
- delete islemi icin bizden delete html olmasini istiyoruz html i ekliyoruz ve yine post fonk override ederek msg ekliyoruz

# ------------------------------------

# Class Based Views

# ------------------------------------

⁡⁢⁢⁢from django.urls import reverse_lazy

from django.views.generic import (
ListView,
CreateView,
DetailView,
UpdateView,
DeleteView,
)

class TodoListView(ListView):
model = Todo
ordering = ['-id'] # template_name = 'todo_list.html' # after 'templates/' default: 'modelname/modelname_list.html'
⁡-------------------------------------------------------------------------
