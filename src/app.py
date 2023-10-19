from src.authentication.Login import Login
from src.users.AdminHandle import Admin
from src.users.ReceptionistHandle import Receptionist
from src.users.DoctorHandle import Doctor
from src.users.PatientHandle import Patient
from src.common.AccountEdit import *
from src.common.CheckPatient import CheckPatient


def main():
    # Authenticate the user
    current_user = Login().auth_user()

    if current_user:
        current_user_id = str(current_user.get("id"))
        privilege_level = current_user.get("privilege_level")

        # Admin functions
        if privilege_level == "1":
            Admin().set_codes()

            # Receptionist functions
        elif privilege_level == "3":
            print(
                "Press 1 to create a patient account\nPress 2 to edit your personal account\nPress 3 to view your personal account\nPress -1 to exit\n"
            )

            while True:
                option = input()

                if option == "1":
                    Receptionist().create_patient_account()
                    print("Press the next number: ")

                elif option == "2":
                    AccountEdit(current_user_id)
                    print("Press the next number: ")

                elif option == "3":
                    view_account(current_user_id)
                    print("Press the next number: ")

                elif option == "-1":
                    print("Thank you, receptionist")
                    break

                else:
                    print("Invalid input. Try again")

            # Doctor functions
        elif privilege_level == "2":
            print(
                "Press 1 to add sickness details\nPress 2 to add a drug prescription\nPress 3 to add a lab test prescription\nPress 4 to view sickness details\nPress 5 to view previous drug prescriptions\nPress 6 to view lab test prescription\nPress 7 to edit your account\nPress 8 to view your account\nPress -1 to exit\n"
            )

            while True:
                option = input()

                if option in ["1", "2", "3", "4", "5", "6"]:
                    while True:
                        patient_id = input("Enter the patient ID: ")

                        if CheckPatient(patient_id):
                            break
                        else:
                            print("Invalid patient ID")

                    if option == "1":
                        Doctor().add_sickness_details(patient_id)
                        print("Press the next number: ")

                    elif option == "2":
                        Doctor().add_drug_prescription(patient_id)
                        print("Press the next number: ")

                    elif option == "3":
                        Doctor().add_labtest_prescription(patient_id)
                        print("Press the next number: ")

                    elif option == "4":
                        Doctor().read_sickness_details(patient_id)
                        print("Press the next number: ")

                    elif option == "5":
                        Doctor().read_drug_prescription(patient_id)
                        print("Press the next number: ")

                    elif option == "6":
                        Doctor().read_labtest_prescription(patient_id)
                        print("Press the next number: ")

                elif option == "7":
                    AccountEdit(current_user_id)
                    print("Press the next number: ")

                elif option == "8":
                    view_account(current_user_id)
                    print("Press the next number: ")

                elif option == "-1":
                    print("Thank you, doctor")
                    break

                else:
                    print("Invalid input. Try again")

            # Patient functions
        elif privilege_level == "4":
            print(
                "Press 1 to update your account\nPress 2 to view your account details\nPress 3 to view sickness details\nPress 4 to view previous drug prescriptions\nPress 5 to view lab test prescription\nPress -1 to exit\n"
            )

            while True:
                option = input()

                if option == "1":
                    AccountEdit(current_user_id)
                    print("Press the next number: ")

                elif option == "2":
                    view_account(current_user_id)
                    print("Press the next number: ")

                elif option == "3":
                    Patient().read_sickness_details(current_user_id)
                    print("Press the next number: ")

                elif option == "4":
                    Patient().read_drug_prescription(current_user_id)
                    print("Press the next number: ")

                elif option == "5":
                    Patient().read_labtest_prescription(current_user_id)
                    print("Press the next number: ")

                elif option == "-1":
                    print("Thank you")
                    break

                else:
                    print("Invalid input. Try again")
