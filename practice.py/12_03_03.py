tests = [
    {"username": "admin", "password": "1234"},
    {"username": "admin", "password": "wrong"},
    {"username": "user", "password": "1234"},
    {"username": "admin", "password": "1234"}
]

users = {
    "admin": "1234",
    "tester": "abcd"
}

for test in tests:
    if test["username"] in users and users[test["username"]]== test["password"]:
        print("Login successful")
    else:
        print("Invalid credentials")