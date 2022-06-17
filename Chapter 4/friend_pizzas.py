my_pizzas = ["cheese", "pepperoni", "pineapple"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("mushroom")
friend_pizzas.append("sausage")

print("My pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\n\nMy friend's pizzas are:")
for pizza in friend_pizzas:
    print(pizza)