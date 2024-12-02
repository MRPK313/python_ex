from pprint import pprint


class UserList(list["User"]):

    def search(self, user_name: str) -> list["User"]:

        matching_user: list["User"] = []
        

        for user in self:
            if user_name in user.user_name:
                matching_user.append(user)
        
        return matching_user
    
    

class User:

    all_users: list["User"] = UserList()
    def __init__(self, user_name: str, email: str, password: str) -> None:
        
        self.user_name = user_name
        self.email = email
        self.password = password

        User.all_users.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r})"

    def __str__(self) -> str:
        return f"{self.user_name}"
    

class Seller(User):

    def order(self, order: "Order") -> None:
        print(f"{self.user_name} from your product {order!r} was sold")
            

class Buyer(User):

    def __init__(self, user_name: str, email: str, password: str, phone: str) -> None:
        super().__init__(user_name, email, password)
        self.phone = phone


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r}, phone={self.phone!r})"






john = User("John", "john@example.com", "John1234")

seler_test = Seller("kate", "kate@example.com", "kate1234")

seler_test2 = Seller("joli", "joli@example.com", "joli1234")

buyer1 = Buyer("larry", "larry@example.com", "larry1234", "0934")


pprint(repr(buyer1.all_users))

