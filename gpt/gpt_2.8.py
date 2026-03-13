logs = [
    "INFO: Login success",
    "ERROR: Payment failed",
    "INFO: Order created",
    "ERROR: Database timeout",
    "INFO: Logout"
]
total_info = 0
total_error = 0
error_logs= []

for log in logs:
    if "ERROR" in log:
        total_error += 1
        error_logs.append(log)
    else:
        total_info += 1

print("Total Info", total_info)
print("Total Error",total_error)
print("Error logs")
for error in error_logs:
    print(error)

