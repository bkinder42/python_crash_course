favorite_languages = {
    "Eve": "Rust",
    "Evan": "Python",
    "Bob": "C++"
}

participants = ["Evan", "Bob","Shodan","Caroline"]

for participant in participants:
    if participant in favorite_languages.keys():
        print(f"Thank you for taking the poll {participant}!")
    else:
        print(f"Please take the poll {participant}!")