# Server Systems

- Physical Servers (BareMetal Servers):

  - Bilgisayar -> Yüksek donanım, özel işlemciler, özel işletim sistemleri.
  - Kurulum: zor
  - VeriTaşıma: zor
  - Maliyet: yüksek
  - Dedicated Servers
  - Barındırma -> Datecenter

- Virtual Servers (VMs: Virtual Machines):

  - Bir fiziksel makina içinde çok sanal makina.
  - Kurulum: orta (iso image)
  - VeriTaşıma: orta
  - Maliyet: orta
  - Bir makiaden diğer makinaya geçiş zorluğu.
  - Hypervisor yazılımları -> vmware.com
  - VPS (Virtual Private Server), VDS (Virtual Dedicated Server)

- Containers:

  - Bir fiziksel/sanal makina içinde çok konteyner.
  - Kurulum: kolay (docker image)
  - VeriTaşıma: kolay
  - Maliyet: düşük
  - Tüm konteynerları aynı ortamdan yönetebilme.
  - Microservice mimarisi.
  - Container yazılımları -> docker.com
  - kubernets kurdugumuz mimariyi yönetmemize olanak sagliyor, docker da ki image ve containerlarin yönetilmesini sagliyor trafik yogunluguna göre calistiracagi programlari yönetebiliyoruz, trafik arttikca container i ac yada hepsini ayni anda calistirma yada yogunluk azalmasiyla aktif containerlarin calismasini azaltabilir

- docker bir yazilimi (herhangi bir sistemi frontend,backend yada bir muhasabe programi da olabilir ) kapali bir kutu haline getirip kopyalayip tasima imkani veren bir sistemdir
- kendi lokalinizde yaptiginiz bir program server a tasidiginizda calismayabilir docker da bu problem kaldirilabiliyor kendi kullandiginiz os bile docker icine gömebilirsiniz
- image; yazilimin tasinabilir kopyalanabilir kapali hali (ziplenmis hali gibi)
- container; yazilimin acilip kullanilabilinen hali
- bir yazilimimiz olacak ve docker build dedigimiz de bu yazilim image haline getirilecek
- fakat bir django projesi dusunelim projeyi githubdan cektikten sonra env,.env.requrement dosyalari yok belki gerekli olan bazi guncellemeler yapilmasi gerekebilir, image aktarmadan önce ayaga kaldirip gereksinimlerini yapmamiz lazim ondan sonra bu calisan hali image cevirmemiz lazim bu noktada docker file devreye giriyor
- docker file da bir projeyi ayaga kaldiran komutlari yazacagiz
- docker sistemine docker run dedigimizde bu docker file i baz alip bu dosya icindekileri gerceklestirip bir image haline getirecek
- docker file yazacagiz proje icin gerekli komutlar burada yazacak ---> sonra buil ile bu bir image haline getirilece----> sonrasinda run diyerek baska bir yerde container uzerinden sistemimiz calisacak
- bir py dosyasi aciyoruz basit bir print komutu yaziyoruz
- projeyi docker image a cevirmek icin bir dockerfile olusturuyoruz
- docker file a yazacagimiz komutlari baz alarak bir image a cevir diyoruz
- bir docker server i actik fakat bos bu yuzden docker image in temeline calistiracagimiz motoru koymamiz (bu proje icin python) from kodu ile aliyoruz
- docker hub a gidip istedigimiz alt yapi yazilimi ariyoruz (bir isletim sistemi gerekirse onu da alabiliriz) bize lazim olacak python surumunu seciyoruz
- kullanmak istedigimiz paketin ismini kopyaliyoruz ve from dan sonra yaziyoruz (run yaptigimizda docker hub a baglanip bu python u getirecek)
- kullanacagimiz dosyalari bir klasörun icine atip calisma alani acmak icin workdir komutu ile klasör ismi veriyoruz (projeyi app klasörune at demis oluyoruz )
- dosyalarimizi göndermek icin copy tag ini kullaniyoruz normalde py dosyamizi bir önceki satirda belirttigimiz klasöre at deriz fakat bir den fazla py dosyamiz icin tek tek yazmayip . . seklinde belirterek verdigimiz yol altindaki butun dosyalari gönder diyoruz
- cmd komutu ile butun dosyalari yukledikten sonra python ile bu app i calistir diyoruz
-

# altyapi icin

FROM python:alpine3.18

# calisma alani

WORKDIR /app

# Dosyalari aktar

# COPY FROM TO

#COPY app.py /app
COPY . .
#Commands
CMD python app.py

- öncelikle docker in durumunu sorgulamak icin
- $ docker --version & docker version & docker info(docker sisteminin altyapi bilgileri)
- $ docker --help (help komut icin herhangi bir komut + help yazarsak onun ile ilgili bilgileri getirir)
- docker file i baz alip image dönusturmek icin
- $ docker build . ( . ile dockerfile in oldugu yeri gösteriyoruz)
- docker sistemindeki imageleri listelemek icin
- $ docker image ls & docker images
- docker da image, container ile ilgili islemler yapmak icin id den ilk 3 karakteri kullanilabilir
- silmek icin
- $ docker rmi 3karekter
- isim vererek image olusturma (ayni isim verirsek digerinin yerine son yazilan gelir ilki silinir)
- $docker build . --tag app & docker build . -t test_app
- image a bir version vermek
- $ docker build . -t test_app:v1
- bir öncekini klonlayip yeni isim verme
- $docker tag test_app test_app:v0.5
- yeni isimlendirmede var olan image korunup uzerine klonlama seklinde yapiyor
- docker images ile listeleyip idlerini görebiliriz
- hepsini silme
- $ docker image prune & docker image prune -a -f (hepsini her sekilde silme -f force)
- container a dönusturme
- $ docker run
- image i belirterek container calistirma
- $ docker run id3karakteri
- container listelemek icin
- $ docker container ls & docker ps -a (calisan containerler gelir)
- duran bir container baslatmak durdurma
- $ docker start 3karktr & docker stop 3 karktr
- container silme
- $docker rm containername
- docker container prune -f (butun containerlari siler)
- interactive mod image i container a cevir, container i calistir, container i acik birak, container icinde bir terminal ac ve disardan container a komut gönderebilelim
- $ docker run it test_image sh
- interactive moddan cik
- $exit
