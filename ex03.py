from typing import List
from functools import reduce

#Ex3 - Adding new atributes to Student, creating College, and creating avarege methods
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
    def __init__(self, name:str, age:int, address: str, course: str, registration_number: int, test1_score: int, test2_score: int, test3_score: int,):
        super().__init__(name=name, age=age, address=address)
        self._course = course
        self._registration_number = registration_number
        self._test1_score = test1_score
        self._test2_score = test2_score
        self._test3_score = test3_score
    
    def return_course(self) -> str:
        return f"Registered in {self._course}"
    
    def change_course(self, new_course: str) -> None:
        if not new_course:
            raise ValueError("Course can't be empty")
        self._course = new_course
    
    def average(self):
        return ((self._test1_score + self._test2_score + self._test3_score)/3)
    
    def aproved(self):
        if self.average() >= 6:
            return True
        return False
    
class College(object):
    def __init__(self, students: List[Student]):
        self.students = students
    
    def general_average(self):
        scores = []
        for student in self.students:
            scores.append(student.average())
        score_sum = reduce(lambda x, y: x + y, scores)
        if len(scores) > 0:
            return (score_sum/len(scores))
        return 0

    def max_avarege(self):
        scores = []
        for student in self.students:
            scores.append(student.average())
        return reduce(lambda x, y:x if x > y else y, scores)
    
    def min_avarege(self):
        scores = []
        for student in self.students:
            scores.append(student.average())
        return reduce(lambda x, y:x if x < y else y, scores)

