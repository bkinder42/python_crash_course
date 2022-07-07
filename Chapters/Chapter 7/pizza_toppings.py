while True:
    pizza_topping = input("Please enter a pizza topping, or enter 'quit' to "
        "end: ")
    if pizza_topping.lower() == "quit":
        break
    print(f"Adding {pizza_topping.title()} to your pizza!\n")