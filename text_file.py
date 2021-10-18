import json


# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as temp_file:
        # First we load existing data into a dict.

        file_data = json.load(temp_file)

        # Join new_data with file_data inside emp_details

        file_data["users"].append(new_data)

        # Sets file's current position at offset.

        temp_file.seek(0)

        # convert back to json.

        json.dump(file_data, temp_file, indent=4)


# write_json(user, filename="user.json")


def read_json(filename='data.json'):
    with open(filename, 'r+') as temp_file:
        # First we load existing data into a dict.

        file_data = json.load(temp_file)

        # Join new_data with file_data inside emp_details

        return file_data["users"]


def write_transaction(new_data, username, filename='data.json'):
    with open(filename, 'r+') as tmp_file:
        # First we load existing data into a dict.

        file_data1 = json.load(tmp_file)
        print(len(file_data1))
        # Join new_data with file_data inside emp_details
        for i in range(0, len(file_data1)):
            if file_data1['transactions'][0]['username'] == username:

                file_data1['transactions'][0]['transaction'].append(new_data)

        # Sets file's current position at offset.

        tmp_file.seek(0)

        # convert back to json.

        json.dump(file_data1, tmp_file, indent=4)


account = 123456789

tmp_usr = read_json(filename='user.json')
print(type(tmp_usr))
print(tmp_usr["account" == account])
sm = tmp_usr["account" == account]
print(type(sm))
print("this is total amount" + sm['amount'])
amount = 10000
# stng = str(amount) + "has been added to " + sm['name'] + "'s account"
stng = "has been added to "

write_transaction(stng, sm['name'], filename='transaction.json')


def find_person(tmp, name):
    # usr1 = [i for i in tmp if name in i]
    # usr1 = {k: v for (k, v) in tmp.items() if k == name}
    # return usr1
    for i in range(0, len(tmp) - 1):
        if tmp[i]['name'] == name:
            return tmp[i]

