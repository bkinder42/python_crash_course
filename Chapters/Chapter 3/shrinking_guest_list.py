guests = ["Evan", "Caroline", "Ada"]
for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")

print("\nLet's add some more guests!\n")

guests.insert(0, "Jane")
guests.insert(2, "Lucretia")
guests.append("Julia")

for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")

print("\nWhoops I can only invite two people!\n")

while len(guests) > 2:
    print(f"Sorry {guests.pop()}, there isn't space for you.")

for guest in guests:
    print(f"Don't worry {guest}, you're still invited.")

del guests[1]
del guests[0]

print(guests)