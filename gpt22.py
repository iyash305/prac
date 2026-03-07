users = {
    "admin" : "1234",
    "tester" : "abcd"
}

def login(username,password):
    if username in users and users[username] == password:
        return True
    else:
        return False

attempts = [
    {"username" : "admin", "password" : "wrong"},
    {"username" : "admin", "password" : "wrong"},
    {"username" : "admin", "password" : "1234"},
    {"username" : "admin", "password" : "1234"}
]

failed_attempts = 0

for attempt in attempts:
    result = login(attempt["username"],attempt["password"])

    if result:
        print("Login successful")
        failed_attempts = 0
        break
    else:
        failed_attempts += 1
        print("Login Failed")

    if failed_attempts == 3:
        print("Account locked")
        break

