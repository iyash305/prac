tests = [
    {"username": "admin", "password": "1234"},
    {"username": "admin", "password": "wrong"},
    {"username": "user", "password": "1234"},
    {"username": "admin", "password": "1234"}
]

correct_username = "admin"
correct_password = "1234"
passed = 0
failed = 0
failed_users= []

for test in tests:
    if test["username"] == correct_username and test["password"] == correct_password:
        passed += 1
        print("Login Successful")
    else:
        failed += 1
        failed_users.append(test["username"])
        print("Invalid Credentials")

print("Passed:",passed)
print("Failed:",failed)
print(f"Failed users:",failed_users)