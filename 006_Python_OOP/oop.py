import os
os.system('cls' if os.name == "nt" else 'clear')
# her code calistiginda terminal ekrani temizler, terminal ekranini alt alta uzatmamak icin kullanilir
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP
# ---------------------------------------------

'''
def print_type(data_list):
    for data in data_list:
        print(data, type(data))


print_type(['yasin', 30, 33.33, True, (1, 2, 3), [2, 3, 4], lambda x:x])
'''

'''
# class olusturma 
class ClassName: #PascalCase isimlendirme

    variable_for_class ='value' 
'''

# ------------------------


class Person:
    name = 'Yasin'
    surname = 'Demir'


print(Person)
print(Person.name)
print(Person.surname)

# Set object from Class:

personel = Person()  # instance = classdan olusturulmus obje

print(personel)
print(personel.name)
print(personel.surname)

print('--------------------')

personel.name = 'jacop'
personel.surname = 'jj'
personel.age = 30  # instance da yapilan degisiklik classda degisiklik yapmaz ama buraya istedigimizi ekleyebiliriz

print('--------------------')

print(personel.name)
print(personel.surname)
print(personel.age)

print('--------------------')

# classda yapilan degisiklikler instance i etkiler fakat tam tersi olmaz
personel_1 = Person()
print(personel_1.name)
Person.name = 'Rafe'
print(personel_1.name)


# ------------------------

personel_2 = Person()

print(personel_1)
print(personel_2)

print('--------------------')

personel_1.name = 'jacop'

print(personel_1.name)
print(personel_2.name)
# bir instance da yapilan degisiklik diger instance i etkilemez

# eger peronel=Person yaparsak () olmadan personel de bir class olmus oluyor ve ondan instance olusturabiliriz

print('--------------------')


class Person:
    name = 'Yasin'
    surname = 'Demir'

    # class lar icinde func ve method olusturabiliyoruz
    # js classindaki this python da self seklinde this global iken self global degil yazacagimiz metot icinde parametre olarak göndermemiz gerekiyor
    # instancedan method cagirirken self parametresi yollanmiyor
    def test(self):
        print(self.name + ' ' + self.surname)


personel_3 = Person()
personel_3.name = 'Jacop'
personel_3.surname = 'jj'
personel_3.test()  # arka planda calisma sekli --> Person.test(personel)

print('--------------------')


class Person:
    name = 'Yasin'
    surname = 'Demir'
    # class icine atanacak ve yazilacak kodlar instance tarafindan kullanilmasini istediklerimiz veya istemediklerimizi belirtebiliyoruz private ve public seklinde
    # underscore ile baslayan degiskenlerin instance tarafindan degistirilmemesi beklenir ama degistirilebiliyor, python bunu piyasa icin getiriyor kendi özgurlukcu yapisini bozmamak icin fakat piyasa private degil ulasilabilr oldugunu görunce yeni bir metod daha bulup double underscore ile yeni bir tanimlama yapiyorlar
    # eger double underscore ile yaziliyorsa private olur disaridan instance ile ulasilamaz
    _path = 'FS'
    __location = 'Sweden'

    # -------get/set
    # get ile baslayanlar getter method, erisim icin kullaniliyor, get veya set yazmak zorunlu degil piyasa standartidir python icin diger metodlari yazmaktan bir farki yoktur
    # setter ile baslayanlar setter method , guncelleme islemi icin kullaniliyor
    def get_location(self):
        return self.__location

    def set_location(self, new_val):
        self.__location = new_val


personel_4 = Person()
# print(personel_4.__location) # bu sekilde calistirirsak ulasamadigi icin hata veriyor
print(personel_4.get_location())
personel_4.set_location('Turkey')
print(personel_4.get_location())


print('--------------------')


class Person:
    name = 'Yasin'
    surname = 'Demir'

# class icinde method tanimladigimizda self parametresi kullanmamiz gerekiyordu fakat methodun kullanimina göre methodu staticlestirip icine self arguman yazmayabiliriz ama istersek farkli argumanlar yazabiliriz

    @staticmethod
    def test():
        print('Hello')


personel_5 = Person()
personel_5.test()

print('--------------------')

# Double-Underscore Methods : DunderMethods


class Person:
    name = 'Yasin'
    surname = 'Demir'

    # dunder a özel bir metoddur
    def __str__(self):
        # return ' this is an instance derived from this class'
        return f'{self.name} {self.surname}'

    # constructor method
    def __init__(self):
        self.name = 'Jacop'
        self.surname = 'JJ'


personel_6 = Person()
print(personel_6)
