users = {
    "admin" : "1234",
    "tester" : "abcd"
}

def login(username,password):
    if username in users and users[username] == password:
        return True
    return False

test_cases = [
    {"username" : "admin", "password" : "1234"},
    {"username" : "tester", "password" : "abcd"},
    {"username" : "admin", "password" : "wrong"}
]

for test_case in test_cases:
    result = login(test_case["username"],test_case["password"])

    if result:
            print("Test case passed")
    else:
             print("Test case failed")
