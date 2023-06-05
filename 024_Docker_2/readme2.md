- backend ve frontend i yapilmis bir projeyi lokalde kaldirip docker da image a cevirecegiz
- backend ve frontend icin terminal ayri ayri acip cd backend cd frontend ile dosyalarin icine giriyoruz cunku bu dosyalarin disinda genelde terminal acmistik
- backend icin pyhton -m venv env ile env klasörunu olusturuyoruz --> source env/Scripts/activate --> pip install -r requirements.txt env dosyasi varsa echo secret_key=sdasdas --> makemigrations --> migrate --> createsuperuser --> runserver acik olarak birakiyoruz
- frontend icin yarn (kurulum icin yeterli) --> 2 terminal de calisir durumda
- terminalleri acik calismak iyi degil cunku terminal herhangi bir durumdan etkilenir terminalleri kapatip docker kismina geciyoruz
- gitignore gibi docker ignore dosyasi aciyoruz actigimiz env klasörunun docker da image a gitmesini istemiyoruz bu sekilde docker image a gitmesini istemedigimiz dosyalar icin dockerignore kullaniyoruz front ve back icin ayri dockerignore olusturuyoruz
- docker image olusturmaya basliyoruz bunun icin kullancagimiz program icin bir docker file olusturuyoruz
- backend den basliyoruz dockerfile = image i buradaki komutlari baz alarak olustur
- backend projemiz bir python oldugu icin python import ederk basliyoruz ayrica docker icinde python calisabilmesi icin 2 tane daha ayar ekliyoruz
- projemiz icin bir klasör olustur ve onun icinde calis diyoruz workdir ile (docker da baska dosyalarla karismasin diye)
- copy . . ile lokaldeki her seyi dockerdaki workdir icine kopyala diyoruz (ilk . lokaldeki dosyalar 2. . ise dockerdaki dosyalar)
- dockerignore da env var butun dosyalri docker a atmayacak fakat bnm projemi calistirmak icin bir env klasörune ihtiyacim var
- cmd docker run yapildiktan sonra aktif hale gelen bir komut
- fkat bize docker build esnasinda env olusturulmali onun icinde run komutunu kullaniyoruz (izole bir ortam icin env kurmamiza gerek yok direk modulleri kurmak yeterli) no cache ile cache olmadan modulleri yukle demis oluyoruz cache yazmasak da sorunsuz calisiyor
- build etmek icin cmd kismina kadar olan kisim yeterli
- cmd docker run yapildigi zaman container a cevirdigi zaman calisacak komut, container acarken projemiz calismasi icin runserver yapiyoruz ve backend deki kullandigimiz port docker da gecerli olmadigi icin 0.0.0.0:8000 portunu kullaniyoruz
- expose disariya port aktarmak icin kullaniliyor kullanilmasa da olur fakar bu sekilde daha yönetilebilir oluyor
- ana klasörde terminal acip docker build ./backed -t backend diyoruz backend klasöru icinde build etsin diye ve -t ile image a isim veriyoruz
- docker desktop acmayi unutmuyoruz
- docker extension da kurdugumuz image geldi
- image i container a cevirmek icin docker run --name backend_con backend en saga calistiracagimiz image in ismi araya da eklemek istedigimiz bir komut olursa onu yaziyoruz
- eger terminalde ctrl c calismassa baska bir terminal acip docker stop yapabiliriz yada container i extension uzerinden durdurabiliriz ayni sekilde docker start komutu da kullanilabilir
- docker system prune -a -f ile image, container ve docker cache sistemi de siliniyor
- image i kapali kutu seklinde 8000 port u ile gönderdik fakat container acildiginda hangi port ile calisacagini söylemedik bunun icin
- docker run -p 8000:8000 backend image name i ekliyoruz icerdeki 8000 ni disardan 8000 ile calistir demis oluyoruz
- bu islemlerden sonra docker container calisiyor ve terminalden görebiliyoruz fakat terminal e mudahale edemiyoruz docker container arka da calismasi icin deamon mode da kullanacagiz docker --help dedigimizde de komutu bulabliriz
- docker run -d -p 8000:8000 backendimagename seklinde yaziyoruz ve container imiz arka planda calisiyoruz vscode kapatsak bile container imiz calismaya devam ediyor
- expose yapinca docker hub uzerinde port degisimi yapabiliyoruz

FROM python:3.10.8-slim-bullseye

# docker icinde pythonun saglikli calisabilmesi icin

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

COPY . .

# no cache optional

RUN pip install -r requirements.txt --no-cache-dir

CMD python manage.py runserver 0.0.0.0:8000
#optional:
EXPOSE 8000

# docker system prune -a -f hepsini siler

- frontend icin docker file aciyoruz
- nodejs icin surumunu giriyoruz
- work dir icin frontend klasöru acmasini istiyoruz
- copy icin lokaldeki ve docker daki olarak
- run icin calistiracagimiz npm install yada yarn install yazabiliriz
- cmd icin container imiz calisacagi zaman yapacagi islem icin npm start || yarn start (container yarn ile calismayabiliyoru bu yuzden npm kullanmak daha saglikli)
- expose icinde 3000 port unu kullaniyoruz
- terminali aciyoruz ayni islemleri frontend icin yaziyoruz
- docker build ./frontend -t frontend_image ile image olusturuyoruz islemler bittikten sonra arka plan calismasi icin frontend de de yapiyoruz
- docker run -d -p 3000:3000 deamon modda portlarimda 3000 ayarlari ile container i mi calistir demis oluyoruz
- dcoker desktop da resource ayarlarindan bilgisayarimizdaki docker in kullanacagi ayarlari degistirebiliriz
- bu islemden sonra frontend ve backend vscode kapali olsa bile calisabiliyor bilgisayarimiz bir nevi server görevi göruyor

FROM node:19-slim

WORKDIR /frontend

COPY . .

RUN npm install

CMD npm start
EXPOSE 3000

- bir server a birden fazla ip giris yapabilir, ip dijital dunyanin yol göstericisi gibi görebiliriz
- örnek olarak tarayici clarusway in server ip sine gidiyor o ip ye karsilik gelen server i buluyor ve clarusway in icerigini istiyor server de html css kodlarini veriyor tarayici da aldigi bu kodlar ile yayin yapiyor
- peki port bu durum da nerede
- bir server var ve bu server a giden bir ip var fkat web server i var email kontrol eden server var yani cesitli serverlar var peki server kendi icerisinde bu yönlendirmeyi nasil yapiyor, iste bu durumda devreye portlar giriyor ip server in kendisine gider portlar da server in icindeki alanlara gider exp 80 portu http portudur , 443 https portudur piyasa standardir bunlar
- docker image silmek icin $ docker rmi 3karakter seklinde idi container acilmis bir image icin önce container i silmemiz lazim onun icin $ docker rm 3 karakter olarak yada tum container lar icin $ docker container prune -f ile yapiyorduk
- 80 portu ile calistirmak icin docker -d -p 80:3000 imagename bundan önce 3000:3000 portunu da acmistik 2 port da aktif olarak calisabiliyor 80 port u default oldgu icin tarayici da sadece localhost olarak calistirabiliyoruz
- docker hub da image gönderip cekmek icin giris yapiyoruz
- terminalden docker hub a girdigimizi belirtmek icin $ docker login yapiyoruz eger desktop da giris yapilmis ve acilmissa otomatik olark algiliyor
- docker hub da manuel bir repo olusturuyoruz repo ismini giriyoruz ve bos repomuz acildi simdi lokaldeki repoyu gönderme islemi yapacagiz ama dirak push reponame ile yapamiyoruz onun icin push pull icin kullaniciadi/reponame seklinde olmali yani $ docker tag backend_image yasind/backend_image seklinde ismini de degistiriyoruz ardindan $docker push yasind/backend_image seklinde push pull islemlerini yapabiliriz
- hub a gittigimizde reponun doldugunu görebiliyoruz
- repo olusturmadan da yeni repo olusturabiliriz $ docker tag backend_image yasind/backend_image2 $ docker push yasind/backend_image2 seklinde yapabiliriz
- docker tag backend_image yasind/backend_image:v1 seklinde guncelleme de yapabiliyoruz push icin docker push yasind/backend_image:v1 seklinde gönderebiliyoruz mevcut reponun icine
- ayni sekilde frontend icinde yapiyoruz
- pull islemi icinde pull yapmamiz yeterli ayni sekilde
- pull yaptiktan sonra imagelari lokale cekmis oluyoruz imagelari calistirmak icin container lari aciyoruz
- $ docker run -d -p 80:3000 frontend image in ilk 3 hanesi ayni islemi backend icinde yapiyoruz ve container lar calismaya basliyor
