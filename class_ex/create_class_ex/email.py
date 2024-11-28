class Email:
    """
    Represents an email with sender, receiver, title, and body.
    """

    def __init__(self, sender: str) -> None:
        """
        Initializes a new Email object.

        Args:
            sender (str): The sender of the email.
        """
        self.sender = sender
        self.receiver = "doesnt set"
        self.title = "doesnt set"
        self.body = "doesnt set"

    def send_email(self, receiver: str, title: str, body: str) -> str:
        """
        Sends an email to the specified receiver with the given title and body.

        Args:
            receiver (str): The receiver of the email.
            title (str): The title of the email.
            body (str): The body of the email.

        Returns:
            str: A string representation of the sent email.
        """
        self.receiver = receiver
        self.title = title
        self.body = body
        return f"receiver: {self.receiver}\nTitle: {self.title}\nBody: {self.body}"

    def __str__(self) -> str:
        """
        Returns a string representation of the Email object.

        Returns:
            str: A string representation of the Email object.
        """
        return f"{self.sender} Send email to {self.receiver}\nTitle: {self.title}\nBody: {self.body}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the Email object in Python syntax.

        Returns:
            str: A string representation of the Email object in Python syntax.
        """
        return f"{self.__class__.__name__}({self.sender!r})"

email1 = Email(sender="john@example.com")
email1.send_email(receiver="Kate@example.com", title="happy death day", body="where is myh Ineritance\nREST IN PEACE")
print(email1)
print(repr(email1))

