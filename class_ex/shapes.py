

class Shape:

    def __init__(self, **kwargs) -> None:
        

        
        for key, value in kwargs.items():
            setattr(self, key, value)


        self.area = None
        self.perimeter = None

    
    def calculate_area(self) -> None:
        pass

    def calculate_perimeter(self) -> None:
        pass

    def show(self) -> str :

        info = f"\n{self}\n"

        for key, value in self.__dict__.items():

            if value != None:
                info += f"{key}: {value: .2f}\n"

        return info
    

    def __str__(self) -> str:
        return self.__class__.__name__


# length, width
class Rectangle(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = self.length * self.width


    def calculate_perimeter(self) -> None:
        self.perimeter = 2 * (self.length + self.width)


# length
class Square(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = self.length ** 2


    def calculate_perimeter(self) -> None:
        self.perimeter = 4 * self.length

    

# base, height, side1, side2
class Triangle(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = (self.base * self.height) / 2


    def calculate_perimeter(self) -> None:
        self.perimeter = self.base + self.side1 + self.side2

    

# diameter1, diameter2, lenght
class Rhombus(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = (self.diameter1 * self.diameter2) / 2


    def calculate_perimeter(self) -> None:
        self.perimeter = self.length * 4
    

# base, height, width
class Parallelogram(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = self.base * self.height


    def calculate_perimeter(self) -> None:
        self.perimeter = (self.base + self.width) * 2
    

# base, height, lheight, side1, side2
class Trapezium(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = (self.height / 2) * (self.lheight + self.base)


    def calculate_perimeter(self) -> None:
        self.perimeter = self.lheight + self.base + self.side1 + self.side2
    

# redius
class Cicle(Shape):

    def __init__(self, **kwargs) -> None:
        
       super().__init__(**kwargs)

    
    def calculate_area(self) -> None:
        self.area = 3.14 * self.redius **  2


    def calculate_perimeter(self) -> None:
        self.perimeter = 2 * 3.14 * self.redius

    



r = Rectangle(length = 2, width = 6)
r.calculate_area()
r.calculate_perimeter()
print(r.show())
print(40 * "_")


s = Square(length = 4)
s.calculate_area()
s.calculate_perimeter()
print(s.show())
print(40 * "_")


t = Triangle(base = 4, side1 = 3, side2 = 5, height = 3)
t.calculate_area()
t.calculate_perimeter()
print(t.show())
print(40 * "_")


m = Rhombus(length = 6, diameter1 = 6, diameter2 = 10)
m.calculate_area()
m.calculate_perimeter()
print(m.show())
print(40 * "_")


p = Parallelogram(base = 6, height = 2, width =4)
p.calculate_area()
p.calculate_perimeter()
print(p.show())
print(40 * "_")


f = Trapezium(base = 8, height = 4, lheight = 5, side1 = 4  , side2 = 5)
f.calculate_area()
f.calculate_perimeter()
print(f.show())
print(40 * "_")


c = Cicle(redius = 4)
c.calculate_area()
c.calculate_perimeter()
print(c.show())
print(40 * "_")