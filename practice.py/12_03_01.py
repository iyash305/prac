entered_username = input("Enter usernmae: ")
entered_password = input("Enter password: ")

username = "admin"
password = "1234"

if entered_username== username and entered_password == password:
    print("Login Succesful")
else:
    print("Invalid Credentials")