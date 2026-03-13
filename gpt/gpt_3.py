response = {
    "status" : 200,
    "user" : "admin",
    "role" : "admin",
    "active" : True
}

expected = {
    "status" : 200,
    "role" : "admin",
    "active" : False
}


total_passed = 0
total_failed = 0

for key in expected:
    if response[key] == expected[key]:
        total_passed += 1
        print("Passed:",key)
    else:
        total_failed += 1
        print("Failed", key)

print("Total passed: ",total_passed)
print("Total failed: ",total_failed)
