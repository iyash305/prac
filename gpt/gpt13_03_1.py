users = {
    "admin": "1234",
    "tester": "abcd"
}

tests = [
    {"username": "admin", "password": "1234"},
    {"username": "admin", "password": "wrong"},
    {"username": "user", "password": "1234"},
    {"username": "tester", "password": "abcd"}
]

for test in tests:
    username = test["username"]
    password = test["password"]

    if username not in users:
        print("User not found")
    elif users[username] == password:
        print("Login succesful")
    else:
        print("Wrong password")