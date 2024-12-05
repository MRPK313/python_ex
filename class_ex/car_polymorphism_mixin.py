class Vehicle:
    """
    A base class representing a vehicle.

    Attributes:
        color (str): The color of the vehicle.
        weight (float): The weight of the vehicle in kilograms.
    """

    def __init__(self, color: str, weight: float, **kwargs) -> None:
        """
        Initialize a Vehicle object.

        Args:
            color (str): The color of the vehicle.
            weight (float): The weight of the vehicle in kilograms.
        """
        self.color = color
        self.weight = weight
    
    def move(self) -> str:
        """
        Abstract method to represent the movement of the vehicle.

        Returns:
            str: A string describing the vehicle's movement.
        """
        raise NotImplementedError("This method must be overridden by subclasses.")

    def __str__(self) -> str:
        """
        Return a string representation of the Vehicle.

        Returns:
            str: A string containing the vehicle's color and weight.
        """
        return f"Vehicle(color={self.color!r}, weight={self.weight!r}kg)"


class Car(Vehicle):
    """
    A class representing a car, inheriting from Vehicle.

    Attributes:
        cylinders (int): The number of cylinders in the car's engine.
    """

    def __init__(self, cylinders: int, **kwargs) -> None:
        """
        Initialize a Car object.

        Args:
            cylinders (int): The number of cylinders in the car's engine.
            **kwargs: Additional keyword arguments passed to the parent class.
        """
        super().__init__(**kwargs)
        self.cylinders = cylinders
    
    def move(self) -> str:
        """
        Describe the movement of the car.

        Returns:
            str: A string indicating that the car is driving.
        """
        return "Car is driving."

    def __str__(self) -> str:
        """
        Return a string representation of the Car.

        Returns:
            str: A string containing the car's color, weight, and number of cylinders.
        """
        return f"Car(color={self.color!r}, weight={self.weight!r}kg, cylinders={self.cylinders})"


class Airplane(Vehicle):
    """
    A class representing an airplane, inheriting from Vehicle.

    Attributes:
        seats (int): The number of seats in the airplane.
    """

    def __init__(self, seats: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.seats = seats
    
    def move(self) -> str:
        return "Airplane is flying."

    def __str__(self) -> str:
        return f"Airplane(color={self.color!r}, weight={self.weight!r}kg, seats={self.seats})"


class Bicycle(Vehicle):
    """
    A class representing a bicycle, inheriting from Vehicle.

    Attributes:
        length (float): The length of the bicycle.
    """

    def __init__(self, length: float, **kwargs) -> None:
        super().__init__(**kwargs)
        self.length = length
    
    def move(self) -> str:
        return "Bicycle is pedaling."

    def __str__(self) -> str:
        return f"Bicycle(color={self.color!r}, weight={self.weight!r}kg, length={self.length})"


class Benz(Car):
    """
    A class representing a Benz car, inheriting from Car.

    Attributes:
        is_hybrid (bool): Indicates whether the Benz is a hybrid car.
    """

    def __init__(self, is_hybrid: bool, **kwargs) -> None:
        super().__init__(**kwargs)
        self.is_hybrid = is_hybrid
    
    def move(self) -> str:
        return "Benz is driving."

    def __str__(self) -> str:
        return f"Benz(color={self.color!r}, weight={self.weight!r}kg, cylinders={self.cylinders}, is_hybrid={self.is_hybrid})"


# Example usage
if __name__ == "__main__":
    car = Car(color="Red", weight=1500, cylinders=8)
    print(car)
    print(car.move())

    benz = Benz(color="Black", weight=1600, cylinders=6, is_hybrid=True)
    print(benz)
    print(benz.move())
