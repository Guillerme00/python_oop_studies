#Ex2 - Create a Person and Student class, extend Person to Student, and add new features
class Person(object):
    def __init__(self, name:str, age: int, address: str):
        self._name = name
        self._age = age
        self._address = address
    
    def __str__(self) -> str:
        return f"{self._name}, {self._age} years old, lives in {self._address}"
    
    def show_address(self) -> str:
        return f"{self._name} lives in {self._address}"
    
    def change_address(self, new_address: str) -> None:
        self._address = new_address

class Student(Person):
    def __init__(self, name:str, age:int, address: str, course: str, registration_number: int):
        super().__init__(name=name, age=age, address=address)
        self._course = course
        self._registration_number = registration_number
    
    def return_course(self) -> str:
        return f"Registered in {self._course}"
    
    def change_course(self, new_course: str) -> None:
        if not new_course:
            raise ValueError("Course can't be empty")
        self._course = new_course