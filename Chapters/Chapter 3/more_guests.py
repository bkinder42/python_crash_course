guests = ["Evan", "Caroline", "Ada"]
for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")

print("\nLet's add some more guests!\n")

guests.insert(0, "Jane")
guests.insert(2, "Lucretia")
guests.append("Julia")

for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")