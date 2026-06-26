import random

class Precinct:
    def __init__(self, number, detectives, location):
        self.__number = number
        self.__detectives = detectives
        self.__location = location
    
    def get_number(self):
        return self.__number
    
    def get_detectives(self):
        return self.__detectives
    
    def get_location(self):
        return self.__location
    
    def add_detective(self, detective):
        self.__detectives.append(detective)

    def set_location(self, location):
        self.__location = location

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        # On garde les espaces d'indentation pour séparer les détectives entre eux
        separateur = "\n        -------------\n        "
        liste_detectives = separateur.join(str(detective) for detective in self.__detectives)
        
        # On aligne "Location", "Detectives" et le premier trait tout à gauche dans les guillemets
        return f"""-----PRECINCT {self.__number} ------
Location : {self.__location}
Detectives :
        ------
        {liste_detectives}"""
        

class Person:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def add_age(self, years):
        self.__age += years
    
    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight
    
    def set_weight(self, weight):
        self.__weight = weight

class Detective(Person):
    def __init__(self, name, age, weight, height, years_of_service, weapon, quotes):
        Person.__init__(self, name, age, weight, height)
        self.__years_of_service = years_of_service
        self.__weapon = weapon
        self.__quotes = quotes

    def get_weapon(self):
        return self.__weapon
    
    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_years_of_service(self):
        return self.__years_of_service
    
    def add_years_of_service(self, years):
        self.__years_of_service += years

    def add_age(self, years):
        super().add_age(years)
        self.add_years_of_service(years)

    def call_detective(self):
        quote = random.choice(self.__quotes)
        print(f"[Phone Call with {self.get_name()}]")
        print(f'   "{quote}"\n')

    def __str__(self):
        return f"""Name : {self.get_name()}
        Age : {self.get_age()}
        Height : {self.get_height()} cm
        Weight : {self.get_weight()} kg
        Years of service : {self.__years_of_service}
        Weapon : {self.__weapon.get_name()} (Caliber: {self.__weapon.get_caliber()}mm)"""


class Weapon:
    def __init__(self, name, caliber, age):
        self.__name = name
        self.__caliber = caliber
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def add_age(self, years):
        self.__age += years
    
    def get_age(self):
        return self.__age
    
    def get_caliber(self):
        return self.__caliber
    
if __name__ == "__main__":
    Pistol = Weapon("Villiers 9mm Pepperbox Pistol", 9, 18)
    Service_Kiejl = Weapon("Kiejl Armistice Service Pistol", 9, 5)
    Interurban = Weapon("Bell-Mouth Interurban", 11, 8)


    harry_quotes = [
        "Detective. Arriving. On. The. Scene.",
        "I am the law."
    ]

    kim_quotes = [
        "Don’t fuck with Kim Kitsuragi.",
        "God, please.",
        "Sunrise, Parabellum."
    ]

    jean_quotes = [
        
    ]

    judit_quotes = [
        
    ]


    Harry = Detective("Harrier Du Bois", 44, 180, 90, 26, Pistol, harry_quotes)
    Kim = Detective("Kim Kitsuragi", 43, 175, 68, 4, Pistol, kim_quotes)
    Jean = Detective("Jean Vicquemare", 41, 182, 75, 18, Service_Kiejl, jean_quotes)
    Judit = Detective("Judit Minot", 38, 170, 60, 11, Service_Kiejl, judit_quotes)

    Precinct41 = Precinct(41, [Harry, Kim, Jean, Judit], "Jamrock")
    print(Precinct41)
    Harry.call_detective()
    Kim.call_detective()