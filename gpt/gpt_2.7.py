users = {
    "admin": {"password": "1234", "role": "admin"},
    "tester": {"password": "abcd", "role": "tester"},
    "dev": {"password": "xyz", "role": "developer"}
}

tests = [
    {"username": "admin", "password": "1234"},
    {"username": "tester", "password": "wrong"},
    {"username": "dev", "password": "xyz"},
    {"username": "guest", "password": "1111"}
]

for test in tests:
    username = test["username"]
    password = test["password"]
    if username in users:
        if password == users[username]["password"]:
            role = users[username]["role"]
            print(username,"Login Succesful",role)
        else:
            print("Wrong Password")
    else:
        print(username, "Not Found")
