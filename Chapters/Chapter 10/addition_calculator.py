while True:
    while True:
        try:
            num1 = int(input("Enter a number: "))
        except ValueError:
            print("That's not a number! Try again!")
        else:
            break

    while True:
        try:
            num2 = int(input("Enter another number: "))
        except ValueError:
            print("That's not a number! Try again!")
        else:
            break

    print(f"{num1} + {num2} = {num1+num2}!\n")

    keep_going = input("Would you like to continue (y/n)? ")
    if keep_going == 'n':
        break