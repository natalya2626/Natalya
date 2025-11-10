class Human:                                        # класс человек 
    def __init__(self, title, age):
      
        self._title = title
        self._age = age
        
    
class Builder(Human):                               # класс строитель
    def __init__(self, title, age, buildind_count):
        super().__init__(title, age)
        self._building_count = buildind_count  
        
    def build(self):
        print('build_hom')         
             
class Sailor(Human):                                # класс моряк
    def __init__(self, title, age, sail_circumnavigation):
        super().__init__(title, age)
        self._sail_circumnavigation = sail_circumnavigation
        
    def sail(self):
        print('swim_circumnavigation')   #   circumnavigation- кругосветка
    
    
class Pilot(Human):                                    # класс  пилот 
    def __init__(self, title, age, flies_count):
        super().__init__(title, age) 
        self._flies_count
        
    def fly(self):
        print('fly')                        