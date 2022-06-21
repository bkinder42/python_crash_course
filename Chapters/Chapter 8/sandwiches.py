def make_sandwich(*toppings):
    print("Making a sandwich with: ")
    for topping in toppings:
        print(f" - {topping.title()}")

make_sandwich("Lettuce", "Tomato", "Bacon")
make_sandwich("Peanut butter", "jelly")
make_sandwich("tuna")