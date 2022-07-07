class User:
    def __init__(self, username, first_name, last_name, department, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email
        self.login_attempts = 0

    def describe(self):
        print(f"User information for {self.username}: ")
        print(f"\tFirst Name: {self.first_name}\n"
                f"\tLast Name: {self.last_name}\n"
                f"\tDepartment: {self.department}\n"
                f"\tEmail: {self.email}\n")

    def greet(self):
        print(f"Good morning {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

sam = User("ssepiol1", "Sam", "Sepiol", "Office of the CTO", "sam@e-corp.com")

sam.increment_login_attempts()
sam.increment_login_attempts()
print(sam.login_attempts)
sam.reset_login_attempts()
print(sam.login_attempts)