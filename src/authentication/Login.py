import json
from src.common.HashHandle import hash_password

class Login:
    @staticmethod
    def auth_user():
        while True:
            name = input("Enter username: ")
            hashed_password = hash_password(input("Enter password: "))

            try:
                with open("config.json", "r") as json_data_file:
                    data = json.load(json_data_file)

                    for user in data["users"]:
                        if name == user["name"] and hashed_password == user["password"]:
                            current_user = user
                            print("Login successful!")
                            return current_user
                    else:
                        print("Login failed. Check your credentials and try again.")
            except FileNotFoundError:
                print("Configuration file not found. Please check your setup.")

if __name__ == "__main__":
    current_user = Login().auth_user()
    if current_user:
        print("Logged in as:", current_user["name"])
    else:
        print("Login failed. Exiting.")
