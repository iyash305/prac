class Loginsystem:
    def __init__(self):
        self.users = {
            "admin" : "abcd",
            "tester" : "1234"
        }

    def login(self,username,password):
        if username in self.users and self.users[username] == password:
            return True
        return False
    
system = Loginsystem()

test_cases = [
    {"username" : "admin", "password": "abcd"},
    {"username" : "tester","password" : "1234"},
    {"username" : "admin", "password" :"wrong"}
]

for case in test_cases:
    result = system.login(case["username"],case["password"])

    if result:
        print("Test case passed")
    else:
        print("Test case failed")