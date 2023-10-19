from src.common.HashHandle import *
import json


class Admin:

    def set_codes(self):
        doctor, receptionist = '', ''
        print("Press 1 to edit the doctor code\nPress 2 to edit the receptionist code\nPress 3 to create an admin account\nPress -1 to exit\n")
        while True:
            role_number = input()
            if role_number == '1':
                doctor = hash_password(input("Enter the new doctor code: "))
                print("Doctor code updated successfully.")
                print("Press the next number: ")
            elif role_number == '2':
                receptionist = hash_password(input("Enter the new receptionist code: "))
                print("Receptionist code updated successfully.")
                print("Press the next number: ")
            elif role_number == '3':
                self.create_admin()
                print("Admin account created successfully.")
                print("Press the next number: ")
            elif role_number == '-1':
                print("Thank you, admin.")
                break
            else:
                print("Invalid input")

        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            doc_code = data['codes'].get('doctor')
            rec_code = data['codes'].get('receptionist')
            if doctor:
                doc_code = doctor
            if receptionist:
                rec_code = receptionist
            data['codes'] = {
                'doctor': doc_code,
                'receptionist': rec_code,
            }

        with open("config.json", 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def create_admin():
        name = input('Admin username: ')
        temp_password = hash_password(input('Temporary password: '))

        # Read and write user to the config file
        with open("config.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            admin_id = len(data['users']) + 1
            data['users'].append({
                'id': admin_id,
                'name': name,
                'password': temp_password,
                'user_type': "admin",
                'privilege_level': '1'
            })
        with open("config.json", 'w') as outfile:
            json.dump(data, outfile)

        print("Admin account created successfully.")
        print("Please enter personal details of admin")

        admin_name = input('Admin name: ')
        age = input('Age: ')
        nic_no = input('NIC number: ')
        tel = input('Telephone number: ')

        # Read and write admin details to the data file
        with open("data.json", 'r') as json_data_file:
            data = json.load(json_data_file)
            data['personal_details'].append({
                'id': admin_id,
                'name': admin_name,
                'age': age,
                'nic_no': encode(nic_no),
                'tel': encode(tel)
            })
        with open("data.json", 'w') as outfile:
            json.dump(data, outfile)
