file_path = "resources/guest.txt"

name = input("What is your name? ")

with open(file_path, "a") as file:
    file.write(f"{name}\n")

    