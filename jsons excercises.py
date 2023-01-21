# the "ABC" module provides a set of abstract base classes that can be
# used to define interfaces or to provide a standard way of subclassing
# certain classes. This means that you can use these ABCs to specify the
# methods and properties that a class must implement, without having to
# provide a complete implementation for those methods and properties.
#
# For example, let's say you have a base class called "Shape" that defines
# an interface for classes that represent geometric shapes. The Shape class
# might define methods like area() and perimeter() that calculate the area and
# perimeter of the shape, respectively. However, these methods would not have a
# specific implementation in the Shape class, because the way to calculate the
# area and perimeter of a shape can vary depending on the specific type of shape.
# Instead of providing an implementation for the area() and perimeter() methods
# in the Shape class, you can use the "ABC" module to define the Shape class as
# an abstract base class. This means that any class that subclasses Shape must
# implement the area() and perimeter() methods, but the Shape class itself does
# not provide an implementation for those methods.
import math
# Here is an example of how you might define the Shape class as an abstract base class using the "ABC" module:

from abc import ABC, abstractmethod


class Shape:
    def __init__(self, units, color):
        self._units = units
        self._color = color

    def get_color(self):
        return self._color

    def get_units(self):
        return self._units

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape, ABC):
    def __init__(self, height, width, units, color):
        super().__init__(units, color)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


# In this example, the Shape class is defined as a subclass of the ABC class from the
# "ABC" module. This makes it an abstract base class. The @abstractmethod decorator is
# used to indicate that the area() and perimeter() methods are abstract and must be
# implemented by any subclasses of Shape.
# If you try to create an instance of the Shape class directly, you will get an error
# because the class is abstract and cannot be instantiated. However, you can create
# subclasses of Shape that provide an implementation for the area() and perimeter()
# methods. These subclasses can then be instantiated and used normally.
# For example, you could define a Circle class that extends Shape and provides an
# implementation for the area() and perimeter() methods:

class Circle(Shape):
    def __init__(self, radius, units, color):
        super().__init__(units, color)
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius


# In this example, the Circle class is a subclass of Shape and therefore must implement the area()
# and perimeter() methods. The __init__() method is used to initialize the Circle instance with a
# given radius. The area() and perimeter() methods use the radius to calculate the area and perimeter
# of the circle, respectively.
# Once you have defined the Circle class, you can create an instance of it and use the area()
# and perimeter() methods to calculate the area and perimeter of the circle:


# the Shape class is defined as a subclass of the ABC class from the "ABC" module, which makes
# it an abstract base class. The Shape class defines an __init__() method that initializes a Shape
# instance with a given set of units and color, as well as two abstract methods: area() and perimeter().
# These methods do not have a specific implementation in the Shape class
# and must be implemented by any subclasses of Shape.
#
# The Rectangle class is defined as a subclass of Shape. This means that the Rectangle class must implement the area()
# and perimeter() methods defined in the Shape class. The Rectangle class also has its own __init__() method, which is
# used to initialize a Rectangle instance with a given height, width, units, and color. The __init__() method uses the
# super() function to call the __init__() method of the Shape class and pass the units and color arguments to it.
#
# Once you have defined the Shape and Rectangle classes, you can create an instance of the Rectangle class and use
# its area() and perimeter() methods to calculate the area and perimeter of the rectangle:
#

r = Rectangle(5, 10, "cm", "blue")
print(r.area())    # prints 50
print(r.perimeter())    # prints 30


# In this example, the r variable is assigned to an instance of the Rectangle class,
# initialized with a height of 5, a width of 10, a unit of "cm", and a color of "blue".
# The area() and perimeter() methods are called on this instance to calculate the area and perimeter of the rectangle,
# respectively. These methods must be implemented in the Rectangle class, but they can use the height, width, and units
# attributes inherited from the Shape class to perform the calculation.

