rivers = {
    "nile": "egypt",
    "potomac": "united states",
    "ural": "russia"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs in {country.title()}.")