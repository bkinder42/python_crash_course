pets = [
    {
        "owner": "ben",
        "name": "sonic",
        "type": "hedgehog",
        "age": 10
    },
    {
        "owner": "evan",
        "name": "tang",
        "type": "soda",
        "age": 8
    },
    {
        "owner": "shodan",
        "name": "buttercup",
        "type": "horse",
        "age": 22
    }
]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type']} who is {pet['age']} "
        f"years old named {pet['name'].title()}!")