class City:
    def __init__(self, city_name, region_name, country_name, number_of_citizens, zip_code, area_code):
     self.city_name = city_name
     self.region_name = region_name
     self.country_name = country_name
     self.number_of_citizens = number_of_citizens
     self.zip_code = zip_code
     self.area_code = area_code





    def location(self):
        print(f"{self.name} sa nachadza v {self.occupation}")

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov a pracujem ako ")
    def zostarni(self, kolko):
        age = self.age + kolko
        self.age = age
        print(f"Novy vek je {age}")

    def vypis(self):
        print(f"{self.name} + {self.age} + {self.gender} + {self.occupation}")
class Student(Person):
    def __init__(self, name, age, gender, occupation, score):
        super().__init__(name, age, gender, occupation)
        self.score = score

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self.gender}")
        else:
            print(f"{self.name} nie je genius a {self.gender}")


patrik = Student("Patrik", 30, "muz", "Bratislava", 95)


dalibor = Student("Dalibor", 27, "muz", "Bratislava", 80)
print(dalibor.vypis())
patrik.name = "Milan"
print(dalibor.jeGenius())
patrik.pozdrav()
patrik.zostarni(10)
dalibor.location()

print(patrik.age)
