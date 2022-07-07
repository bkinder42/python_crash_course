guests = ["Evan", "Caroline", "Ada"]
for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")

print("\nWhoops, Caroline can't make it. Time to make a new list.\n")

guests.remove("Caroline")
guests.append("Jane")

for guest in guests:
    print(f"Hello {guest}, would you like to come to dinner?")