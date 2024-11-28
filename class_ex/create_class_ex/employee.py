class Employee:
    """
    Represents an employee with name, salary.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new Employee object.

        Args:
            name (str): The name of the employee.
        """
        self.name = name
        self.salary = 0.0

    def set_salary(self, new_salary: float) -> str:
        """
        Sets the new salary for the employee.

        Args:
            new_salary (float): The new salary for the employee.

        Returns:
            str: A string representation of the Employee object.
        """
        if new_salary > 0.0:
            self.salary = new_salary

        return self.__str__()

    def __str__(self) -> str:
        """
        Returns a string representation of the Employee object.

        Returns:
            str: A string representation of the Employee object.
        """
        return f"Employee name: {self.name}, Salary: {self.salary}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Employee object in Python syntax.

        Returns:
            str: A string representation of the Employee object in Python syntax.
        """
        return f"{self.__class__.__name__}({self.name!r})"
    


engineer = Employee("John")

engineer.set_salary(50000)

print(engineer)

print(repr(engineer))