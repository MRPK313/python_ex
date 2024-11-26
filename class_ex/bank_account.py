# import random
# import datetime

# random.seed(datetime.datetime.now().timestamp())
# print(random.random())
# print(datetime.datetime.now().timestamp())


class BankAccount:

    last_account = 0

    def __init__(self, name: str) -> None:
        """
        for initialize member by name , balance , account_number
        """

        self.account_number = BankAccount.last_account + 1
        BankAccount.last_account += 1

        self.name = name
        self.balance = 0.0

    def __str__(self) -> str:
        return f"account_number: {self.account_number} , name: {self.name} , balance: {self.balance}"

    def deposit(self) -> str:
        add_balance = float(input("Enter balance add : "))
        self.balance += add_balance
        return self.__str__()

    def withdraw(self) -> str:
        withdraw_balance = float(input("Enter number balance withdraw : "))
        if withdraw_balance <= self.balance:
            self.balance -= withdraw_balance
            answer = self.__str__()
        else:
            answer = "balance not enough to withdraw"

        return answer


def main():
    ali = BankAccount("ali")

    hasan = BankAccount("hasan")

    reza = BankAccount("reza")

    while True:

        choice = input("Enter THe Choice number\n1 -> deposit\n2 -> withdraw\n3 -> see balance\n0 -> exit\n")

        if choice == "0":
            break
        elif choice == "1":
            print("-"*40)
            print(ali.deposit())
            print("-"*40)
        elif choice == "2":
            print("-"*40)
            print(ali.withdraw())
            print("-"*40)
        elif choice == "3":
            print("-"*40)
            print(ali)
            print("-"*40)
        else:
            print("-"*40)
            print("unknown choice")
            print("-"*40)

    # print(hasan)

    # print(reza)


if __name__ == "__main__":
    main()
