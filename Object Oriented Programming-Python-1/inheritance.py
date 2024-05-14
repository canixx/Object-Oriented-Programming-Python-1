from abc import ABC , abstractmethod

#inheritance

class Shape(ABC):
    """
     Shape = superclass/ abstract class
    """
    #abstract method

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    #polymorphism and overriding

    def toString(self):pass

#child
class Square(Shape):
    "subclass"
    def __init__(self,edge):
        self.__edge =edge

    def area(self):
        result = self.__edge**2
        print("Area of square:",result)

    def perimeter(self):
        result = self.__edge*4
        print("Perimeter of square:",result)

    #override ve polymorphism
    def toString(self):
        print("Square edge:", self.__edge)

#child
class Circle(Shape):
    "circle class"

    #constant variable
    PI=3.14

    def __init__(self,radius):
        self.__radius= radius

    def area(self):
        result = self.PI*self.__radius**2
        print("Area of circle:", result)

    def perimeter(self):
        result = 2*self.PI*self.__radius
        print("Perimeter of circle:", result)

    def toString(self):
        print("Circle radius:", self.__radius)

c1 = Circle(5)
c1.area()
c1.perimeter()
c1.toString()

s1 = Square(5)
s1.area()
s1.perimeter()
s1.toString()




