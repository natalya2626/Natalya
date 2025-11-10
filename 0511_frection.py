# класс дробь
#  Создайте ласс«Дробь».Необходимо ранить в полях 
# класса: числитель изнаменатель.Реализуйтеметодыкласса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса. Также создайте 
# методы класса для выполнения арифметических опера
# ций (сложение, вычитание, умножение, деление, и т.д.)

class Fraction:
    def __init__(self, numerator, denominator):
      
        self._numerator = numerator
        self._denominator = denominator
        
    def input_data(self):  
        self._numerator = int(input())
        self._denominator = int(input()) 
         
    @property
    def numerator(self):
        return self._numerator
    @property
    def denominator(self):
        return self._denominator    
    
    def multiply(self, other: 'Fraction'):
        return Fraction(self.numerator * other.numerator , self.denominator * other.denominator)
    
        
    def division(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
    
    def add(self, other: 'Fraction'):
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, 
                        self.denominator * other.denominator)
    
    def sub(self, other: 'Fraction'):
        return Fraction (self.numerator * other.denominator - other.numerator * self.denominator, 
                        self.denominator * other.denominator)   
    def __str__(self):
        return f"{self._numerator} {self._denominator}"   
    
a = Fraction(3, 5)
b = Fraction(5, 8)
print(a.add(b))

