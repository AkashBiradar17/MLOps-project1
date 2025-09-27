from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    

p1 = Person("Akash", 25)
print(p1)   # Person(name='Akash', age=25)
