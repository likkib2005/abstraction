from abstraction_demo import Vehicle
class Bike(Vehicle):
    def __init__(self, n, color):      
        super().__init__(n)            
        self.color = color
    def start(self):                   
        print("start with kick")
class Scooty(Vehicle):
    def __init__(self, n):             
        self.no_of_tyres = n
    def start(self):                 
        print("Self Start")
class Car(Vehicle):
    def __init__(self, n):         
        self.no_of_tyres = 2
        self.no_of_gears = 6
    def start(self):               
        print("Start with key")