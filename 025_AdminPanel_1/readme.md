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
# to create gitignore file
- touch .gitignore
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

- app ekledikten sonra settings e gidip secret key icin config import ediyoruz
- ardindan .env icine secret key ekliyoruz
- installed app a product ekliyoruz
- migrate yapiyoruz ve migrate ile db.sqlite3 geliyor
- model yada token ekledigimizde makemigrations yapmamiz gerekiyor
- admin panel uzerinde calisacamiz icin rf ye kullanmayacagiz
- admin icin superuser ile devam ediyoruz
- a panelde calisacagimiz icin url de kullanmayacagiz
- model ekledigimiz icin makemigrations ve migrate yapiyoruz
- product modelini a.panelde görmek icin admin site register yapmamiz gerekiyor ve modeli de import ediyoruz
- hazir veri kullanmak icin faker install yapiyoruz modelden sonra freeze (bazi moduller installdan sonra settings e eklenmiyor onun icin dokumanina bakmak gerekiyor)
- product altinda faker dosyasi aciyoruz ve kodlari yapistiriyoruz
- faker i calistirmak icin shell i kullaniyoruz
- panel icin olan calismalari admin.py da yapacagiz
- admin panelinde gördugumuz butun basliklari,tablolari istedigimiz gibi degistirip stillendirebilyoruz
- admin.site.site_title ile sitenin title ve header , index basligini degistirebilyoruz
  ⁡⁢⁢⁢admin.site.site_title = 'Admin Panel Title'
  admin.site.site_header= 'A.P Header'
  admin.site.index_title='Index Page'⁡

- modelimizin arka planda nasil calistigina bakmak icin model yazdigimiz satirda register a ctrl ile tiklayip fonk icinde ne yazildigina bakiyoruz
- modelimizin yanina admin sayfasinda bir class belirtmedigimiz icin default olan class i kullaniyor kod a gidip baktigmizda admin_class yada modelAdmin kullan dedigini göruyoruz ve model admine gidip ne gecerli olduguna bakiyoruz
- model admin de ise bazi degiskenler ve onlara tanimlanmis özellikler oldugunu göruyoruz
  ⁡⁢⁢⁢class ModelAdmin(BaseModelAdmin):
  """Encapsulate all admin options and functionality for a given model."""

      list_display = ("__str__",)
      list_display_links = ()
      list_filter = ()⁡
      ⁡⁢⁣⁢kucukbir kismi sadece⁡

- admin panelde gösterilen özellikleri buradan degistirebilirz
- modelimizin altina göruntuleyecegimiz veriyi str den cek diyoruduk strdan cekme komutu ise listdisplayde göruyoruz
- bu özellikleri degistirmek icin override yapacagiz
- default modeli inherit edecek sekilde yeni bir class yazacagiz ve degisiklikleri onun icinde yapacagiz
- modelAdmin i geldigi yerden import edebiliriz diger basamaklari yazarak fakat admin sayfasinda admin komple cagirilmis ve admin dosyasindaki init.py a baktigimizda modeladmin in cagirildigini göruyoruz o yuzden tekrardan import etmeye gerek yok
- isim veriyoruz ve admin icindeki model admini inherit ediyoruz, model admine gidip display listi kopyaliyoruz
- modelimizde neler listelenmesini istiyorsak icine yaziyoruz (normalde str dan alacakti ) yazdigimiz modelimize gidip ona göre istedigimz gibi duzenleyebiliyoruz
- fakat bunlari yazip kaydettigmizde panelde yapilan degisiklikler gelmiyor cunku yazdigimiz class i kullandigimizi register a bildirmemiz gerekiyoru register in yazildigi yere gittigimizde admin_class in none oldugunu görmustuk ve site.register yaninda modelimizin yanina yazdigimiz yeni class i da veriyoruz
- tablomuzun sutunlarini degistirmis olduk
- list editable da ekliyoruz bu bize tablo icine girmeden guncelleme imkani verecek ve icine degistirmek istedigmiz bilgi ne ise onu koyuyoruz stockta olanlarin arka rengi bile degisti bu sekilde
- kaydimizin detaylarina gitmek icin id ye tikliyoruz bunu mesela name e tiklayinca detaylara gitme ayari yapmak icin modeladminden link kismini alip degistiriyoruz bunlar liste olduklari icin liste icinde ekleme yapabiliyoruz
- filtreleme eklemek icin yine modeladminden filtreleme kismini aliyoruz istedigimiz filtrelemeleri kullanabliyoruz
- arama icinde search field ekliyoruz
  -ordering icin modeladminden degil onun da basi olan basemodelden alip yaoiyoruz cunku moodeladmin icinde de basemodel admin var onun icinden de alabiliyoruz degisiklik yapmak istedigimiz sey icin, basina - koymak tersten siralama yapiyor
- sayfa basi kayit gösterme sayisini da degisitiriyoruz (pagination api icin )
- arama kismi icin yardimci yazi ekleyebiliyoruz
- bir product detayina girdigimizde slug bölumu var (seo dostu url kucuk harf aralarinda - var) slug field da benzer bir isi göruyor ve biz o bölumu doldururken otomatik olarak url ye uygun yazmasi icin ekleme yapabiliyoruz ve yazdigimiz kodda isme göre slug tipini ayarla demis oluyoruz ve slug da olusan sekilde bir url mizi kurabiliriz
- data hierarcy ile tarihsel hiyerarsik bir sekilde urunleri listeleyebiliriz
- urun detay sayfasina girdigimizde baslik input seklinde alt alta oldugunu göruyoruz bunlari yanyana getirmek istersek fields ve filedset icinde bunun icin fields listesi icine bir liste daha acip satir satir göruntumuzu degistiriyoruz bu basit olarak yaptigimz bir yöntem
- eger daha genis olarak daha fazla ayarlama yapmak istersek fieldset kullanabiliriz ve ayni anda ikisini kullanamayiz ayrica burada verecegimiz ayarla bastigimiz zaman acilip kapanma da ekleyebiliriz bir liste acip her grubu farkli liste icine atiyoruz sonra liste basligi yazip liste icerigine gelecek attributeleri bir dictionary icinde tanimliyoruz class i wide acik sekilde gelsin 2. blum icin de bir tuple daha acip ona da baslik verip optional olarak collapse yapiyoruz ve buraya aciklama da ekleyebliyoruz
- product ekraninda hizli islem menusu var action olan ksim burayi da degistirmemiz mumkun
- model adminde action attribute den yapabiliriz fkat komutlari kullanabilmek icin cagirdigimizda calisacak metodlara da ihtiyacimiz var
- mesela sectigimiz kayitlari stock lara ekleyen yada cikartan bölum icin set_stock_in ve out icin metodlari icin metotlari yapistiriyoruz bir tanesi is_in_stock u true yapiyor digeri false yapiyor yaptiktan sonra da kullaniciya bir mesaj dönuyor yazilacak yaziyida short description ile degistirebiliyoruz
- action kisminda hepsnin secip stokta var veya yok olarak isretle seklinde yapabiliyoruz iki komut ekledigimiz icin iki metod kullanmamiz gerekiyor
- modelde yer almayan veriyi yazdirmak icin onun metodunu yaziyorduk ve onu fields a ekliyorduk serializerda fileds daki basliga göre cagirabiliyorduk ayni sekilde burada da yapabiliriz
- bir metod(fonk) yazdik modelde olmayan bir veriyi göruntulemek istiyoruz urunun ne zman eklendigine dair bu veri db de yok db de created date i tutuyoruz biz suanki tarihten db deki created date i cikartirsak ve onunda gun verisini istersek bize urunun su kadar gundur eklendigi veriyi verecek (serializerdan farki basina get yazmamiza gerek yok ) bu metodu sutunlara eklemek istersek list display i bu metodun altina ekleyip icine ekleyebiliriz yada listenin sonuna ekleyeceksek += seklinde ekleyebiliriz (ama araya yazacaksak butun listeyi eklememiz gerekiyor)
- urunlerin icinde desc alani var buradaki yazilari stillendirmek icin rich text editor kullanacagiz bunun icin ck editor kullanacagiz
- ck editorun django icin bir modulu var onu install yapacagiz pip install django-ckeditor ardindan freeze
- main > serrings > installedapp ckeditor en alta da ayarlarini ekliyoruz CKEDITOR_CONFIGS = {
  'default' : {
  'toolbar' : 'full',
  'height' : 700,
  'width' : 1000
  }
  }
- model e gidip oradaki ck editor icin degisiklikler yapacgiz ve kullancagimiz seyler icin import ediyoruz ve text field i degistiriyoruz blank ve null true lari ekliyoruz
- work gibi bir duzenleme alani geliyor (aslinda bir js editorudur ve arkada o islemleri yapar)
- product altina yeni bir model ekliyoruz review olarak ve product ile bir foreign key iliskisi var, urunun kendisi, yorumlari yayinlansin mi ve ne zaman gibi bilgiler var
- rich text yapisal bir degisiklik degildi fakat model ekledigimiz icin makemigrations ve migrate

class Review(models.Model):
product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
review = models.TextField()
is_released = models.BooleanField(default=True)
created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"

- buraya kadar yaptigimiz islemler product icindi ayni seyleri review icin de yapabiliriz ve en alta review icin ekleme yapiyoruz
- admin site olarak ekle ve reviewadmin modelini de ekliyoruz
- runserver yapinca review de geldi fakat ici bos onun icin faker dan ekleme yapiyoruz (runserver fake verileri görduk)
- urun detaylarina girdigimizde yorumlari da görmek icin bir class yaziyoruz ve admin icinde tabular inline var buda bir urune göre yapilan yorumlari gösteren class onu inherit ediyoruz Tabularinline icine gittigimizde yorumlarin nasil ayarlandigini görebiliyoruz model tanimlanmis bizde icine model tanimliyoruz kullanacagimiz review modeli

# Ürünlerin yorumlarını ürün-detay sayfasında göster:
class ReviewInline(admin.TabularInline): # Alternatif: StackedInline (farklı görünüm aynı iş)
model = Review # Model
extra = 1 # Yeni ekleme için ekstra boş alan
classes = ['collapse'] # Görüntülme tipi (default: tanımsız)

- modeladmin e gittigmiz de inlines diye bir sey var bunu en product modelin altina ekliyoruz ve reviewinline value olarak veriyoruz, classes i collapse oldugu icin kapali geliyor, sayfanin altina urune ait yorumlar gelmis oluyor yorum eklemek icin extra ile bosluk alani verdi bizim icin  
  inlines = [ReviewInline]

- bir urunun kac tane yorumu var onu görmek icin kac dun önce eklendigini görmek icin yazdigimiz metod gibi metod yazip modelin icine ekleyebiliyoruz ve altina da listeleme ekraninin sonuna eklemsi icin += seklinde ekliyoruz ve product sayfasina geldigimizde her urunun kac yorumu oldugunu görebiliyoruz

Kaçtane yorum var:
def how_many_reviews(self, object):
count = object.reviews.count()
return count

    list_display += ['how_many_reviews']

---

class ProductModelAdmin(admin.ModelAdmin):

    # Tablo sutunları:
    list_display = ['id', 'name', 'is_in_stock', 'create_date', 'update_date']
    # Tablo üzerinde güncelleyebilme:
    list_editable = ['is_in_stock']
    # Kayda gitmek için linkleme:
    list_display_links = ['id', 'name']
    # Filtreleme (arama değil):
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # Arama:
    search_fields = ['id', 'name']
    # Default Sıralama:
    ordering = ['-create_date', '-id']
    # Sayfa başına kayıt sayısı:
    list_per_page = 20
    # Arama bilgilendirme yazısı:
    search_help_text = 'Arama Yapmak için burayı kullanabilirsiniz.'
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug' : ['name']}
    # Tarihe göre filtreleme başlığı:
    date_hierarchy = 'create_date'
    # Form liste görüntüleme
    fields = (
        ('name', 'is_in_stock'),
        ('slug'),
        ('description')
    )
    '''
    # Detaylı form liste görüntüleme
    fieldsets = (
        (
            'General Settings', {
                "classes": ("wide",),
                "fields": (
                    ('name', 'slug'),
                    "is_in_stock"
                ),
            }
        ),
        (
            'Optionals Settings', {
                "classes": ("collapse",),
                "fields": ("description",),
                'description': "You can use this section for optionals settings"
            }
        ),
    )
    '''

def set_stock_in(self, request, queryset):
count = queryset.update(is_in_stock=True)
self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')

    def set_stock_out(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ('set_stock_in', 'set_stock_out')
    set_stock_in.short_description = 'İşaretli ürünleri stokta VAR olarak güncelle'
    set_stock_out.short_description = 'İşaretli ürünleri stokta YOK olarak güncelle'

admin.site.register(Product, ProductModelAdmin)

# -----------------------------------------------------

# ReviewModelAdmin

class ReviewModelAdmin(admin.ModelAdmin):
list_display = ('**str**', 'created_date', 'is_released')
list_per_page = 50 # raw_id_fields = ('product',)

admin.site.register(Review, ReviewModelAdmin)
