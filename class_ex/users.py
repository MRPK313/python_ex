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
    def __init__(self, user_name: str, email: str, password: str, **kwargs) -> None:
        
        self.user_name = user_name
        self.email = email
        self.password = password

        User.all_users.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r})"

    def __str__(self) -> str:
        return f"{self.user_name}"
    

class Order:
    pass


class Seller(User):
    def __init__(self,shabba: str, **kwargs) ->None:
        super().__init__(**kwargs)
        self.shabba = shabba
    

    def order(self, order: str) -> None:
        print(f"{self.user_name} from your product {order!r} was sold")
            

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r}, shabba={self.shabba!r})"


class Buyer(User):

    def __init__(self, phone: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.phone = phone


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r}, phone={self.phone!r})"



class SelerAndBuyer(Seller, Buyer):
    def __init__(self, score: str, **kwargs) -> None:

        super().__init__(**kwargs)

        self.score = score

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r}, phone={self.phone!r}, shabba={self.shabba!r}, score={self.score!r})"





john = User("John", "john@example.com", "John1234")

seler_test = Seller(user_name="kate", email="kate@example.com", password="kate1234", shabba="123")

seler_test2 = Seller(user_name="joli", email="joli@example.com", password="joli1234", shabba="123")

buyer1 = Buyer(user_name="larry", email="larry@example.com", password="larry1234", phone="0934")

buyer_and_seler = SelerAndBuyer(user_name="larry", email="larry@example.com", password="larry1234", phone="0934", shabba="65677", score="18")


pprint(buyer1.all_users)

buyer_and_seler.order(order="boock")