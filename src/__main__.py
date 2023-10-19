from src.authentication.SignUp import SignUp
from src.app import main

def login_or_signup():
    while True:
        choice = input("Press 1 to login or 2 to signup: ")

        if choice == '1':
            main()
            break
        elif choice == '2':
            SignUp().create_user()
            print("Login to your account")
        else:
            print("Invalid input. Please enter 1 to login or 2 to signup.")

if __name__ == '__main__':
    login_or_signup()
