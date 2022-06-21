def city_country(city, country):
    result = f"{city.title()}, {country.title()}"
    return result

baltimore = city_country("Baltimore", "United States")
tokyo = city_country("tokyo", "japan")
vancouver = city_country("vancouver", "canada")

print(baltimore)
print(tokyo)
print(vancouver)
