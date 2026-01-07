from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres=n
    @abstractmethod
    def start(self):
        pass
#Vehicle(2) for abstract class object creation is not possible
    def display(self):
        print("I am calling from vehicle class")