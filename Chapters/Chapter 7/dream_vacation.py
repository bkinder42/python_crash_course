destinations = []

while True:
    destination = input("What is your dream vacation destination? ")
    destinations.append(destination)
    keep_going = input("Would anyone else like to answer? (Yes/No): ")
    if keep_going.lower() == "no":
        break

print("\n\nWhat a great list of destinations!")
for destination in destinations:
    print(destination)