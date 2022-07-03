cats = "resources/cats.txt"
dogs = "resources/dogs.txt"

try:
    with open(dogs) as f:
        print(f.read())
except FileNotFoundError:
    print (f"The file {dogs} was not found!")

try:
    with open(cats) as f:
        print(f.read())
except FileNotFoundError:
    print (f"The file {cats} was not found!")