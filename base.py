print("""Welcome To Ferlet Bank
=======================
Please Sign in to your Acount !""")


class User:
    def __init__(self, username, password, ballance):
        self.user = username
        self.pw = password
        self.wallet = ballance

    def DepositAmount(self):
        amount = int(input("Please specify the amount to deposit >> "))
        self.wallet -= amount
        print(f"your new ballance is {self.wallet}")


user001 = User("user1", 1234, 500)
user002 = User("user2", 0000, 5000)
user_list = [user001, user002]
user_found = False

while True:
    current_user = input("Please enter your username >> ")
    for i in user_list:
        if current_user == i.user:
            user_found = True
            current_user = i
            break
    if user_found:
        break
    else:
        print("User Not Found !!")
        continue

print("Found !!!")
current_user.DepositAmount()
