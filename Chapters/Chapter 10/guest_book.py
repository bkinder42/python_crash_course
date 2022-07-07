file_path = "resources/guest_book.txt"

with open(file_path, "a") as file:
    while True:
        guest = input("What is your name? ('stop' to end) ")
        if guest == "stop":
            break
        file.write(f"{guest}\n")

with open(file_path) as file:
    print("Our guests are: ")
    for guest in file.readlines():
        print(f"\t- {guest.rstrip()}")

    
