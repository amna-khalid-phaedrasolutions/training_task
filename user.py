import json_functions


class User:
    limit = 25000
    account_no = None
    __pin = None
    amount = None
    transaction = None

    def __init__(self, account_no, pin, amount):
        self.account_no = account_no
        self.transaction = open("transaction.txt", 'at')
        if len(pin) == 4:
            self.pin = pin
        else:
            print("PIN should contain 4 digits.")
        self.amount = amount

    @staticmethod
    def user_menu(user):
        print("WELCOME TO ACCOUNT MANAGEMENT SYSTEM")
        print("- Press 1 for check you balance.")
        print("- Press 2 for deposit amount.")
        print("- Press 3 for withdraw amount.")
        print("- Press 4 for print statement.")
        print("- Press 5 for send amount to someone.")
        print("- Press 6 for change PIN.")
        print("- Press 7 for see transaction history.")
        print("- Press q for Quit.")
        print ("/nSystem build by AMNA KHALID")
        while True:
            choice = input()
            if choice == 1:
                User.check_amount(user)
            elif choice == 2:
                amount = input("Enter amount: ")
                User.deposit_amount(user, amount)
            elif choice == 3:
                amount = input("Enter amount: ")
                User.withdraw_amount(user, amount)
            elif choice == 4:
                User.print_statement()
            elif choice == 5:
                from_account = input("Enter sender account number: ")
                to_account = input("Enter receiver account number: ")
                tmp_usr = json_functions.read_json(filename='user.json')
                temp1 = json_functions.find_person(tmp_usr, from_account['account'])
                temp2 = json_functions.find_person(tmp_usr, to_account['account'])
                while True:
                    amount = input("Enter amount: ")
                    if amount > User.limit:
                        print("Limit of sending amount is" + str(User.limit) + ", you can't send more than this in one transaction.")
                    else:
                        User.transfer(temp1, temp2, amount)
            elif choice == 6:
                User.change_pin(user)
            elif choice == 7:
                User.show_transactions(user)
            elif choice == 'q':
                exit(0)
            else:
                print("You've entered invalid input, TRY AGAIN")

    @staticmethod
    def deposit_amount(user, amount):
        user['amount'] = int(user['amount']) + amount
        stng = str(amount) + "has been added to " + user['account']
        json_functions.write_tranaction(stng, user['name'], filename='transaction.json')
        print("Amount has done Deposit successfully!! ")
        print("You new Balance is: " + user['amount'])

    @staticmethod
    def withdraw_amount(user, amount):
        user['amount'] = int(user['amount']) - amount
        stng = str(amount) + "has been deducted from " + user['account']
        json_functions.write_tranaction(stng, user['name'], filename='transaction.json')
        print("Amount has done Withdrawn successfully!! ")
        print("You new Balance is: " + user['amount'])

    @staticmethod
    def transfer(from_account, to_account, amount):
        tmp_usr = json_functions.read_json(filename='transaction.json')

        from_account['amount'] = int(from_account['amount']) - amount
        temp = json_functions.find_person(tmp_usr, from_account['account'])
        stng1 = str(amount) + " has been deducted from " + from_account['account']
        temp['transaction'].extend(stng1)

        to_account['amount'] = int(to_account['amount']) + amount
        temp = json_functions.find_person(tmp_usr, to_account['account'])
        stng2 = str(amount) + " has been added to " + to_account['account']
        temp['transaction'].extend(stng2)

    @staticmethod
    def check_amount(user):
        print("You total amount is : " + user['amount'])

    @staticmethod
    def print_statement():
        print("Here is you account statement: "
              "It is a long established fact that a reader will be distracted by the readable content of a page when "
              "looking at its layout. "
              "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, "
              "as opposed to using 'Content here, content here', making it look like readable English. "
              "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, "
              "and a search for 'lorem ipsum' will uncover many web sites still in their infancy. "
              "Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected "
              "humour and the like).")

    @staticmethod
    def change_pin(user):
        while True:
            current_pin = input("Enter current PIN: ")
            if user['pin'] == current_pin:
                new_pin = input("Enter new 4 digits PIN: ")
                if len(str(new_pin)) == 4:
                    user['pin'] = new_pin
                    break
                else:
                    print("Enter 4 digits PIN: ")

            else:
                print("You've entered invalid pin, TRY AGAIN")

    @staticmethod
    def show_transactions(user):
        tmp_usr = json_functions.read_json(filename='transaction.json')
        temp = json_functions.find_person(tmp_usr, user['name'])
        print(temp['transaction'])


