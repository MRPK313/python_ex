

class Rectangle:
    """ create a rectangle
    """

    def __init__(self, length: float, width: float) -> None:

        """ for Rectangle constructor """


        self.length = length
        self.width = width

    def area(self) -> float:
        """ for Area constructor

        Returns:
            float: Area
        """

        return self.width * self.length

    def perimeter(self) -> float:
        """ for Perimeter constructor

        Returns:
            float: Perimeter
        """

        return (self.width + self.length) * 2

    def __str__(self) -> str:
        
        return f"Rectangle width : {self.width} , length : {self.length} , area : {self.area()} , perimeter : {self.perimeter()}"
    
    def __repr__(self) -> str:

        return f"{self.__class__.__name__}({self.length!r} , {self.width!r})"
    




rectangle = Rectangle(20 , 30)

print(rectangle)    # Client-friendly representation

print(repr(rectangle))  # Developer-friendly representation



        