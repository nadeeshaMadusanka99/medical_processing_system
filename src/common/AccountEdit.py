import json
from src.common.HashHandle import *


def AccountEdit(user_id):
    new_name = input('Enter new name: ')
    new_age = input('Enter new age: ')
    new_tel = input('Enter new telephone number: ')

    # read and write new account details to data file
    with open("data.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for i in range(len(details)):
            if user_id == str(details[i]['id']):

                details[i]['name'] = new_name
                details[i]['age'] = new_age
                details[i]['tel'] = encode(new_tel)

    with open("data.json", 'w') as f_outfile:
        json.dump(f_data, f_outfile)

    print("Account updated successfully")


def view_account(user_id):
    # read account details from data file
    with open("data.json", 'r') as data_file:
        f_data = json.load(data_file)
        details = f_data['personal_details']
        for i in range(len(details)):
            if user_id == str(details[i]['id']):
                print("Account name: " + details[i]['name'])
                print("Age: " + details[i]['age'])
                print("NIC number: " + decode(details[i]['nic_no']))
                print("Telephone: " + decode(details[i]['tel']))

    print("Account viewed successfully")



