"""
Multiple Inheritance and Method Resolution Order
"""

class MyBase:
    def __init__(self):
        print("Base.__init__")

class Sup1(MyBase):
    def __init__(self, a, **kwargs):
        print("Sup1.__init__")
        self.a = a
        super().__init__(**kwargs)
        
class Sup2(MyBase):
    def __init__(self, b, **kwargs):
        print("Sup2.__init__")
        self.b = b
        super().__init__(**kwargs)
    
class Sub1(Sup1, Sup2):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)
        


sub1 = Sub1(10, 20)
# Sub1.__mro__
# Sub1.mro()
# # sub1.__class__.mro()
# print(sub1.__class__.mro())
# sub1.a
print(Sup1.mro())
print(Sup2.mro())
print(sub1.a, sub1.b)



class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from 
# the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


pyramid = RightPyramid(base=2, slant_height=4)
pyramid.area()