places = {
    "ben": ["alaska", "baltimore", "japan", "california"],
    "evan": ["shower", "bed", "dreams"]
}

for person in places:
    print(f"{person.title()}'s favorite places are:")
    for place in places[person]:
        print(f"\t{place.title()}")