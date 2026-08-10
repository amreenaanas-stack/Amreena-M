#abstraction is a data hiding--------------------------------------
# through in inheritence

from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def makes_sound(self):
        print("animal makes sound")
class Dog(Animal):
    def __init__(self):
        pass
    def makes_sound(self):
        print("woff woff")
d = Dog()
d.makes_sound()