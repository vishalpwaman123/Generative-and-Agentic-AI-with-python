from recipes.flavors import chai_order
message, price = chai_order("ELACHAI_CHAI", 5)
print(f"{message}, Price {price}")
message, price = chai_order("GINGER_CHAI", 5)
print(f"{message}, Price {price}")