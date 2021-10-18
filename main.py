import json
from datetime import datetime

from admin import Admin
from user import User
import json_functions


def welcome():
    transaction = {

    }
    users = {

    }

    with open("transaction.json", "a") as json_file:
        json.dump(transaction, json_file)

    print("WELCOME TO ACCOUNT MANAGEMENT SYSTEM")
    print("- Press 1 if you're user.")
    print("- Press 2 if you're admin.")
    print("- Press q for Quit.")
    print("")
    print ("System build by AMNA KHALID")

    while True:
        choice = input()
        if choice == 1:
            print("WELCOME TO ACCOUNT MANAGEMENT SYSTEM")
            print("- Press 1 for existing user.")
            print("- Press 2 to create new user.")
            print("- Press q for Quit.")
            print ("System build by AMNA KHALID")

            usr_choice = input()

            if usr_choice == 1:
                account = input("Enter account number: ")
                pin = input("Enter 4 digits PIN number: ")
                tmp_usr = json_functions.read_json(filename='user.json')
                test = tmp_usr['account' == account]
                if test['pin'] == str(pin):
                    User.user_menu(test)
            elif usr_choice == 2:
                name = input("Enter Username: ")
                account = input("Enter account number: ")
                pin = input("Enter 4 digits PIN number: ")
                amount = input("Enter amount: ")
                user = {"name": name,
                        "account": account,
                        "pin": pin,
                        "amount": amount
                        }
                user_trans = {
                    "username": name,
                    "transaction": [

                    ]
                }
                json_functions.write_json(user_trans, "transactions", filename='transaction.json')
                json_functions.write_json(user, "users", filename="user.json")
                tmp_usr = json_functions.read_json(filename='user.json')
                User.user_menu(tmp_usr['name' == name])

        elif choice == 2:
            print("WELCOME TO ACCOUNT MANAGEMENT SYSTEM")
            print("- Press 1 for login.")
            print("- Press 2 to create new admin.")
            print("- Press q for Quit.")
            print ("System build by AMNA KHALID")

            admin_choice = input()

            if admin_choice == 1:
                name = input("Enter username: ")
                pin = input("Enter 4 digits PIN number: ")
                tmp_usr = json_functions.read_json(filename='admin.json')
                test = tmp_usr['username' == name]
                if test['pin'] == str(pin):
                    Admin.admin_menu(test)
            elif admin_choice == 2:
                Admin.add_admin()
                tmp_usr = json_functions.read_json(filename='admin.json')
                test = tmp_usr['username' == name]
                Admin.admin_menu(test)

        elif choice == 'q':
            exit(0)
        else:
            print("You've entered invalid input, TRY AGAIN.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    welcome()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
