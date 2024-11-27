

class Car:
    """A class to represent a car
    """

    def __init__(self) -> None:
        
        self.brand = "Not specified Add this with set_info method"
        self.model = "Not specified Add this with set_info method"
        self.date = "Not specified Add this with set_info method"

    def set_info(self , brand: str, model: str, date: str) -> None:

        self.brand = brand
        self.model = model
        self.date = date

    def get_info(self) -> str:
        
        return f"Your Car  brand: {self.brand}, model: {self.model}, date: {self.date}"

    def __str__(self) -> str:
        
        return f"Your Car  brand: {self.brand}, model: {self.model}, date: {self.date}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
    


mercedes = Car()

mercedes.set_info("Benz", "C-class", "2024")

print(mercedes)


