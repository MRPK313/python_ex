from datetime import datetime, timedelta

# instance method
# class method
# static method

class Product :

    # instance method
    def __init__(self, product_name, price, off) -> None:
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self) -> str:
        return self.product_name


class Comment:

    website_name = "test.com"

    # instance method
    def __init__(self, product, name, description, likes, dislikes) -> None:

        self.product = product
        self.name = name
        self.description = description
        self.likes = likes
        self.dislikes = dislikes
        self.date = datetime.now()


    # instance method
    def show(self):
        
        print(f"product : {self.product}\n"
               f"name : {self.name}\n"
               f"description : {self.description}\n"
               f"likes : {self.likes}\n"
               f"dislike : {self.dislikes}\n"
               f"date : {self.date} s")
        
    # class method
    @classmethod
    def info(cls):
        print(cls.website_name)

        
    # class method
    @classmethod
    def censorship(cls, product, name, description, likes, dislikes):
        
        print("your comment wae censored")
        sc = description.replace("censor test","*"*len(description))
        return cls(product, name, sc, likes, dislikes)

        
    # static method
    @staticmethod
    def alapsed_time(time):

        print(f"alapsed time : {datetime.now() - time}")






print("_"*40)
laptop = Product("loq", 59, 0)

c1 = Comment(laptop, "john", "g00d censor test", 50, 50)

c1.show()

c1.info()



print("_"*40)
laptop = Product("loq", 59, 0)

c1 = Comment.censorship(laptop, "john", "g00d censor test", 50, 50)

c1.show()

c1.info()

print("_"*40)
c1.alapsed_time(c1.date - timedelta(days= 4, minutes= 30))

