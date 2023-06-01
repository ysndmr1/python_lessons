* https://docs.docker.com/get-started/docker_cheatsheet.pdf

```sh

    $ docker --version
    $ docker version

    $ docker info
    
    $ docker --help
    $ docker help
    $ docker build --help

    $ docker search <imagename>

```

```sh
    
    # Image build et:
    $ docker build .
    # Image build et ve image'a isim ver:
    $ docker build . --tag <imagename>
    $ docker build . -t <imagename>
    # Image build et ve image'a isim:sürüm ver:
    $ docker build . -t <imagename>:v2
    $ docker build . -t <imagename>:v2 --no-cache

    # Image'leri listele:
    $ docker images ls
    $ docker images
    # Image sil:
    $ docker rmi <imagename>
    $ docker rmi <imagename> -f
    # Image'leri sil (kullanılmayanlar):
    $ docker images prune
    # Image tag ekle/değiştir:
    $ docker tag <imagename> <newimagename>

    # Image'den Container aç:
    $ docker run <imagename>
    # Image'den Container aç ve container'a isim ver:
    $ docker run --name <containername> <imagename>

    # Container'leri listele:
    $ docker container ls
    $ docker ps
    # Container'leri listele (tümü):
    $ docker container ls -a
    $ docker ps -a
    # Container başlat/durdur:
    docker start|stop <containername>
    # Container sil:
    $ docker rm <containername>
    $ docker rm <containername> -f
    # Container'leri sil (kullanılmayanlar):
    $ docker images prune

    # Interaktif modda aç:
    $ docker run -it <imagename> sh
    # Interaktif moddan çık:
    $ exit

```
