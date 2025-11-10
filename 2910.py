# Задание 1
#  Реализуйте класс «Человек». Необходимо хранить в 
# поляхкласса:ФИО,датурождения,контактныйтелефон, 
# город, страну,домашнийадрес.Реализуйте методы класса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса

class Person:
    def __init__(self,
        full_name, date_of_birth,
        contact_phone_number, city,
        country, home_address
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone_number = contact_phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

 
         
    def input_data(self):  
        self.full_name = input()
        self.date_of_birth = input()
        self.contact_phone_number = input()
        self.city = input()
        self.country = input()
        self.home_address = input()
    
    def __str__(self):
        return f"{self.full_name} {self.date_of_birth} {self.contact_phone_number} {self.city} {self.country } {self.home_address}"
    

a = Person(
    full_name = None, date_of_birth = None,
        contact_phone_number = None, city = None,
        country = None, home_address = None
)   

a.input_data()
print(a)
