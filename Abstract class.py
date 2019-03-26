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


s = Rectangle(5, 7)
print(s.area())
print(s.perimeter())

