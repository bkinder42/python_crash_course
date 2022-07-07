while True:
    age = input("What is your age (or 'quit' to end): ")
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("Your ticket is free!\n")
    elif age >= 3 and age <= 12:
        print("Your ticket is $10.\n")
    else:
        print("Your ticket is $15.\n")