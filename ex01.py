class Person(object):
    def __init__(self, name:str, age: int, adress: str):
        self.name = name
        self.age = age
        self.adress = adress
    
    def __str__(self):
        return f"{self.name}, {self.age} years old, live in {self.adress}"
    
    def show_adress(self):
        print(f"{self.name} live in {self.adress}")
    
    def change_adress(self, new_adress: str):
        self.adress = new_adress

person_1 = Person(name="Guilherme", age=20, adress="Brazil")

print(person_1)
person_1.show_adress()
person_1.change_adress(new_adress="Brazil/SP")
person_1.show_adress()
