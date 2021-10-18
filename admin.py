import json_functions
from user import User


class Admin:
    def __init__(self, username, pin, email):
        self.username = username
        self.pin = pin
        self.email = email
        self.active = True

    @staticmethod
    def admin_menu():
        print("WELCOME TO ACCOUNT MANAGEMENT SYSTEM")
        print("- Press 1 see details.")
        print("- Press 2 for all transactions.")
        print("- Press 3 for delete account.")
        print("- Press 4 for freeze account.")
        print("- Press 5 for set transaction limit.")
        print("- Press 6 for see report.")
        print("- Press q for Quit.")
        print ("/nSystem build by AMNA KHALID")
        while True:
            choice = input()
            if choice == 1:
                Admin.add_admin()
            elif choice == 2:
                Admin.show_details(Admin)
            elif choice == 3:
                Admin.show_transactions()
            elif choice == 4:
                Admin.delete_account(Admin)
            elif choice == 5:
                Admin.freeze_account(Admin)
            elif choice == 6:
                Admin.set_limit()
            elif choice == 7:
                Admin.show_report()
            elif choice == "q":
                exit(0)
            else:
                print("You've entered invalid input, TRY AGAIN")

    @staticmethod
    def add_admin():
        name = input("Enter Username: ")
        pin = input("Enter 4 digits PIN number: ")
        tmp_usr = json_functions.read_json(filename='admin.json')
        temp = json_functions.find_person(tmp_usr, name)
        if temp is not None:
            print("this user is already exist")
            exit(-1)

        admin = {"name": name,
                 "pin": pin,
                 }

        json_functions.write_json(admin, "admins", filename="admin.json")
        print("New admin has successfully added.")

    @staticmethod
    def show_details(admin):
        tmp_usr = json_functions.read_json(filename='admin.json')
        temp = json_functions.find_person(tmp_usr, admin['name'])
        print("Your username: " + temp['username'] + "Email address: " + temp['pin'])

    @staticmethod
    def show_transactions():
        trans = json_functions.read_json(filename='admin.json')
        print(trans)

    @staticmethod
    def delete_account(admin):
        tmp_usr = json_functions.read_json(filename='admin.json')
        temp = json_functions.delete_person(tmp_usr, admin['name'])

    @staticmethod
    def freeze_account(admin):
        tmp_usr = json_functions.read_json(filename='admin.json')
        temp = json_functions.delete_person(tmp_usr, admin['name'])
        temp['active'] = False

    @staticmethod
    def set_limit():
        limit = input("Enter the limit which you want to set for users.")
        User.limit = limit
        print(str(limit) + "has been set as limit of User's Transactions.")

    @staticmethod
    def show_report():
        print("here report will be given.")
