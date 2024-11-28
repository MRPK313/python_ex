class Book:
    """
    Represents a book with title, author, and release year.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The release year of the book.
    """

    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The release year of the book.
        """
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        self.title = title
        self.author = author
        self.year = year

    def get_info(self) -> str:
        """
        Get a formatted string containing the book's details.

        Returns:
            str: Information about the book.
        """
        return f"'{self.title}' by {self.author}, published in {self.year}"

    def __str__(self) -> str:
        """
        Returns a string representation of the Book object.

        Returns:
            str: A string representation of the Book object.
        """
        return self.get_info()

    def __repr__(self) -> str:
        """
        Returns a string representation of the Book object in Python syntax.

        Returns:
            str: A string representation of the Book object in Python syntax.
        """
        return f"{self.__class__.__name__}({self.title!r}, {self.author!r}, {self.year!r})"



book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
print(book1)      
print(repr(book1))
