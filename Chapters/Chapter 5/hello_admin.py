users = ("joe", "bob", "alice", "eve", "ada", "admin", "shodan")

if users:
    for user in users:
        if user.lower() == "admin":
            print("\nHello admin, Evil Eve and Shodan have been detected!!!\n" + 
            "RED ALERT!!!\n")
        elif user.lower() == "eve" or user.lower() == "shodan":
            print(f"Warning {user.title()}: You have been identified as a " +
            "threat and admin has been notified")
        else:
            print(f"Welcome {user.title()}")