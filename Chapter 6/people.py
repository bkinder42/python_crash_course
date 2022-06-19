people = [
    {
        "name": "Butcher",
        "age": 45,
        "city": "New York"
    },
    {
        "name": "Marie",
        "age": 32,
        "city": "Paris"
    },
    {
        "name": "Evan",
        "age": 51,
        "city": "Prauge"
    }
]

for person in people:
    print(f"I know that {person['name'].title()} is {person['age']} "
        f"and lives in {person['city'].title()}.")

