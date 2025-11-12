class Passport:
    def __init__(self,number, name, surname,  ):
        
        self._series = series
        self._number = number
        self.surnamer = surname
        
        
class ForeignPassport(Passport):
    def __init__(self, series, number,visa_information,foreign_passport):
        super().__init__(series, number) 
        self._visa_information = visa_information 
        self.foreign_passport = foreign_passport   
    def build(self):
        print('build_hom')       
        
        