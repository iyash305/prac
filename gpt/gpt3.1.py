class User:
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
        self.failed_attempts = 0

    def login(self,entered_password):
        if self.failed_attempts >= 3:
            print("Account locked")
            return
        
        if entered_password == self.password:
            print("Login Succesful! Role: ",self.role)
            self.failed_attempts = 0
        else:
            print("Login failed")
            self.failed_attempts += 1
        if self.failed_attempts >= 3:
            print("Account locked")


u1 = User("Yash", "1234", "admin")
u1.login("1234")

u2 = User("Admin1", "2345", "tester")
u2.login("1234")
u2.login("1234")
u2.login("1234")
