class User:
    def __init__(self, username, first_name, last_name, department, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.email = email

    def describe(self):
        print(f"User information for {self.username}: ")
        print(f"\tFirst Name: {self.first_name}\n"
                f"\tLast Name: {self.last_name}\n"
                f"\tDepartment: {self.department}\n"
                f"\tEmail: {self.email}\n")

    def greet(self):
        print(f"Good morning {self.first_name.title()}!")

bob = User("bob1", "Bob", "Johnson", "Procurement", "bob@e-corp-usa.com")
sam = User("ssepiol1", "Sam", "Sepiol", "Office of the CEO", "sam@e-corp.com")
shodan = User("shodan", "Shodan", "Master", "AI/ML", "shodan@e-corp.com")

bob.greet()
bob.describe()

sam.greet()
sam.describe()

shodan.greet()
shodan.describe()