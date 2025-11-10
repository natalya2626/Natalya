#  Задание 2
#  Создайте класс «Город». Необходимо хранить в по
# лях класса: название города, название региона, название 
# страны, количество жителей в городе, почтовый индекс 
# города,телефонный код города.Реализуйте методы класса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класс

class City:
    
    def __init__(self,
        title, region_name,
        country_name, number_inhabitants_city,
        city_postal_code, telephone_area_code
    ):
        self.title = title
        self.region_name = region_name
        self.country_name = country_name
        self.number_inhabitants_city = number_inhabitants_city
        self.city_postal_code = city_postal_code
        self.telephone_area_code = telephone_area_code

    
    def input_data(self):  
        self.title = input()
        self.region_name = input()
        self.country_name = input()
        self.number_inhabitants_city = input()
        self.city_postal_code = input()
        self.telephone_area_code = input()
    def __str__(self):
        return f"{self._name} {self.region_name} {self.country_name} {self.number_inhabitants_city} {self.city_postal_code} {self.telephone_area_code}"
    
a = City(
    title = None, region_name = None,
        country_name = None, number_inhabitants_city = None,
        city_postal_code = None, telephone_area_code = None
    
)
a.input_data()
print(a)
      