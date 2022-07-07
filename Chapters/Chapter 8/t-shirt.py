def make_tshirt(message, size='large'):
    print(f"I will print a {size} shirt with the message '{message}'.")

make_tshirt("Positional", "Medium")
make_tshirt(size="X-Large",message="Keyword")
