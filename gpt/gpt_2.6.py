tests =[
    {"username":"admin","password": "1234"},
    {"username":"admin","password": "wrong"},
    {"username": "tester", "password":"abcd"},
    {"username":"tester","password":"wrong"}
]

users = {
    "admin" : "1234",
    "tester" : "abcd"
}     

passed = 0
failed = 0
failed_users = []

for test in tests:
    if users[test["username"]] == test["password"]:
        passed += 1 

    else:
        failed += 1
        failed_users.append(test["username"])

print("Passed:", passed)
print("Failed:",failed)
print("Failed users:")
for user in failed_users:
    print(user)