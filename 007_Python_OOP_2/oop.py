import os
os.system('cls' if os.name == "nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP - 2
# ---------------------------------------------
# Encapsulation : Kapsulleme, ayni amac icin kullanilan degisken ve methodlar bir class icinde yaziliyor
# Abstraction : soyutlama kodlarin gizliligi ve birbirinden bagimsiz calismalari


class Person:
    company = 'Clarusway'

    def __init__(self, name, age, gender='Male'):
        self.name = name
        self.age = age
        self.gender = gender
        print('Personel created')

    def __str__(self):
        return f'{self.name} - {self.age}'

    def get_detail(self):
        return f'{self.name} - {self.age} - {self.gender} - {self.company}'


person_1 = Person('yasin', 30)  # bir classin atandigi degiskene instance denir
print(person_1)
print(person_1.get_detail())


# en son yazmistik fakat siralama olarak employee uzerinde tanimlanmasi gerektigi icin yukariya aldik
class Department:

    def set_department(self, department):
        self.department = department


class Employee(Person):  # person classinin tum özellikleri employee classina aktarilir inheritance

    salary = 5000

    def set_salary(self, salary):
        self.salary = salary

    def __init__(self, name, age, gender, salary, department='AWS'):
        # Super(),inherit ettigimiz ilk class dan itibaren buldugu ilk init methodunu calistirir ve self yazmaktan kurtarir
        # self.name = name
        # self.age = age
        # self.gender = gender
        # self.salary = salary
        super().__init__(name, age, gender)
        # yukarida departmeni aldigimiz icin burda da calistirabilmek icin eklememiz gerekiyor ve init icine parametre olarak da vermemiz gerekiyor
        Department.set_department(self, department)
        # göndermedigimiz parametreyi de asagida degistirdik
        self.salary = salary
        print('Personel created')

    # mevcut bir metodu tekrar tanimlama override denir, yeni metodun eski metodu ezmesi.
    # python overload desteklemez
    def get_detail(self):
        return f'{self.name} - {self.age} - {self.salary} - {self.gender}- {self.department} - {self.company}'


# person_2 = Employee('Jacop', 33, 'Male')
# person_2.set_salary(2000)
# print(person_2.get_detail())

person_3 = Employee('Jace', 33, 'Male', 1500,)
print(person_3.get_detail())
