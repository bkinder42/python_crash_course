sandwiches = ["grilled cheese", "black forest ham", "BLT", "tomato salad"]
finished_sandwiches = []

while len(sandwiches) > 0:
    sandwich = sandwiches.pop()
    print(f"I made your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

print("\n\nI finished making all of the sandwiches! Here's what I made: ")

for sandwich in finished_sandwiches:
    print(sandwich)
