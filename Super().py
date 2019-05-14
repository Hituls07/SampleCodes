"""
Exploring Super() in python
"""
from abc import ABC, abstractclassmethod

class Shape(ABC):
    #  Inherited ABC to make this class as Abstract class

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    @abstractclassmethod
    #  Abstract method is used to make this area method mandatory fpr inheritance classes
    def area(cls):pass

    #  Abstract method is used to make this perimeter method mandatory fpr inheritance classes
    @abstractclassmethod
    def perimeter(cls):pass


class Rectangle(Shape):

    def __init__(self, length, width, **kwargs):
        super().__init__(**kwargs)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def kkk(self):
        return 'Rectangle'


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def kkk(self):
        return 'Square'

class Cube(Square):

    def area(self):
        # Using super(), calling methods of super classes
        face_area = super().area() # re-used area of square (parent class) rather than calculating
        return face_area * 6

    def volume(self):
        # super() can be used with parameters as well
        face_area = super().area()
        return face_area * self.length

    def k(self):

        """
        This should be used to start searching for matching method at one level above in hierarchy.
        arg1 : Subclass
        arg2 : Refers to object
        """
        print('super() without any parameters: {}'.format(super().kkk()))
        print('super() with any parameters: {}'.format(super(Square, self).kkk()))
        """
        In second scenario instead of looking in Square class it started searching in Rectangle class')
        """

s = Cube(5)
print(s.area())
print(s.volume())
print(Cube.__mro__)
print(s.k())