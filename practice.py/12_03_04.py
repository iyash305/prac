class User:
    def __init__(self,username,role):
        self.username = username
        self.role = role

    def display_info(self):
        print("Username",self.username,"Role:",self.role)

class Admin(User):
    def __init__(self,username):
        super().__init__(username,role="QA")
     




a1 = Admin("yash")
a1.display_info()