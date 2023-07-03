print("""Welcome To Ferlet Bank
=======================
Please Sign in to your Acount !
********************************
""")


class User:
    def __init__(self, username, password, ballance):
        self.user = username
        self.pw = password
        self.wallet = ballance

    def DepositAmount(self):
        amount = int(input("Please specify the amount to deposit >> "))
        self.wallet += amount
        print(f" =>  your new ballance is {self.wallet}")

    def WithdrawAmount(self):
        amount = int(input("Please specify the amount to Withdraw >> "))
        self.wallet -= amount
        print(f" =>  your new ballance is {self.wallet}")


user001 = User("user1", 1234, 500)
user002 = User("user2", 0000, 5000)
user_list = [user001, user002]
user_found = False
user_auth = False
# Var in menu
selected_item = 0

while True:
    current_user = input("Please enter your username >> ")
    for i in user_list:
        if current_user == i.user:
            user_found = True
            current_user = i
            break
    if user_found:
        for x in range(3):
            entered_password = int(input("Please Enter Your Password >> "))
            if entered_password == current_user.pw:
                print("Login Successfull")
                user_auth = True
                break
        if user_auth:
            break
        else:
            print("Login Failed, Try Again!")
            pass
    else:
        print("User Not Found !!")
        continue

print("Found !!!")
while True:
    print("""=================================
Please Select one Option from bellow:""")
    print("""1 to See Wallet
2 to Deposit Money
3 to Withdraw Money
9 to Exit""")
    selected_item = int(input('>>> '))
    if selected_item == 9:
        print('GoodBye !')
        break
    elif selected_item == 2:
        current_user.DepositAmount()
    elif selected_item == 1:
        print(' =>  your Ballance is ' + str(current_user.wallet))
    elif selected_item == 3:
        current_user.WithdrawAmount()
    else:
        print('Make sure you enter item number from the menue')
    input('Press Enter to Continue !')
