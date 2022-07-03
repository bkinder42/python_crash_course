import json

filename = "resources/favorite_number.json"

def new_favorite_number(filename):
    favorite_number = input("What is your favorite number? ")

    with open(filename, "w") as f:
        json.dump(favorite_number, f)

def read_favorite_number(filename):
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

favorite_number = read_favorite_number(filename)
if favorite_number:
    print(f"Your favorite number is {favorite_number}!")
    correct = input("Is that number correct (y/n)?")
    if correct == "y":
        print("Yippee!")
    else:
        new_favorite_number(filename)
        print("I'll remember your favorite number!")
else: 
    new_favorite_number(filename)
    print("I'll remember your favorite number!")



