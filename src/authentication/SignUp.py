import json
from src.common.HashHandle import *

class SignUp:
    roles = {'1': "doctor", '2': "receptionist"}

    def create_user(self):

        name = input('Enter a username: ')
        password = input('Enter a password that includes an uppercase letter, a lowercase letter, a digit, and has a minimum length of 6 characters: ')

        # Validate password strength
        while not (any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 6):
            password = input("Password is too weak. Please re-enter: ")

        safe_password = hash_password(password)

        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            doc_code = data['codes'].get('doctor')
            rec_code = data['codes'].get('receptionist')

        # Create hotel staff accounts using the relevant code for security
        while True:
            role_number = input('Press 1 for "doctor account" or 2 for "receptionist account": ')
            
            if role_number == '1':
                code = hash_password(input("Please enter the doctor code to create the account: "))
                if code == doc_code:
                    user_type = self.roles.get('1')
                    privilege_level = '2'
                    break
                else:
                    print("Invalid code")
            elif role_number == '2':
                code = hash_password(input("Please enter the receptionist code to create the account: "))
                if code == rec_code:
                    user_type = self.roles.get('2')
                    privilege_level = '3'
                    break
                else:
                    print("Invalid code")
            else:
                print("Invalid input. Try again")

        # Read and write user information to the config file
        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            user_id = len(data['users']) + 1
            data['users'].append({
                'id': user_id,
                'name': name,
                'password': safe_password,
                'user_type': user_type,
                'privilege_level': privilege_level
            })
        with open("config.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Account created successfully")

        print("Fill in personal account details")
        acc_name = input('Your name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')

        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': user_id,
                'name': acc_name,
                'age': age,
                'nic_no': encode(nic_no),
                'tel': encode(tel)
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Account completed")
