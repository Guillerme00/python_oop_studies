#Creating Person class with 3 atributes and 2 methods
class Person(object):
    def __init__(self, name:str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"{self.name}, {self.age} years old, live in {self.address}"
    
    def show_address(self):
        print(f"{self.name} live in {self.address}")
    
    def change_address(self, new_address: str):
        self.address = new_address

person_1 = Person(name="Guilherme", age=20, address="Brazil")

print(person_1)
person_1.show_address()
person_1.change_address(new_address="Brazil/SP")
person_1.show_address()
