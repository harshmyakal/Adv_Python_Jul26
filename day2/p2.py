from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod 
    def area(self):
        pass
        
    @abstractmethod
    def perimeter(self):
        pass
        
    def description(self):
        # Added () to call the method instead of referencing the method object
        return f"This shape has area {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
circle = Circle(5)
print("Area of Circle:", circle.area())
print(circle.description())