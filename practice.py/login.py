class User:
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.is_locked = False
        self.failed_attempts = 0

    def login(self,input_username,input_password):
        if self.is_locked:
            print("Account is locked")
            return False
        
        if input_username == self.username and input_password == self.password:
            self.failed_attempts = 0
            return True
        
        self.failed_attempts += 1
        print(f"Login failed. Attempt {self.failed_attempts}/3")

        if self.failed_attempts >= 3:
            self.is_locked = True
            print("Account is locked")
        
        return False
        
        
class Admin(User):
    def __init__(self,username,password,role):
        super().__init__(username,password)
        self.role = role

    def login(self,input_username,input_password):
        result = super().login(input_username,input_password)
        if result:
            print("Admin login succesful")
        return result

e1= Admin("Yash","Pass","Admin")
print(e1.login("Yash","Pass1"))
print(e1.login("Yash","Pass2"))
