tests = [
    {"name": "login_test", "status": "passed"},
    {"name": "signup_test", "status": "failed"},
    {"name": "payment_test", "status": "passed"},
    {"name": "logout_test", "status": "failed"},
    {"name": "profile_test", "status": "passed"}
]
passed = 0
failed = 0
failed_test=[]
for test in tests:
    if test["status"] == "passed":
        passed += 1
    else:
        failed +=1
        failed_test.append(test["name"])
print("Total Tests:",len(tests))
print(f"Passed cases: ",passed)
print(f"Failed cases: ", failed)
print("Failed Tests:")
for name in failed_test:
    print(name) 