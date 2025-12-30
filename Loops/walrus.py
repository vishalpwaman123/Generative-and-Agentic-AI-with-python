#Without Walrus

value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")

################# With Walrus #####################

# EXAMPLE 1

value = 13
if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")

# EXAMPLE 2

available_size = ["small", "medium", "large"]

if(requested_size := input("Enter your chai cup size : ")) in available_size:
    print(f"Serving {requested_size} chai")
else:
    print(f"{requested_size} is unavailable")

# EXAMPLE 3

flavors = ["masala", "ginger", "lemon", "mint"]
print(f"Available flavors : {flavors}")

while (requested_flavor := input("choose your flavor : ")) not in flavors:
    print(f"Sorry, {requested_flavor} not available")

print(f"You choose {requested_flavor} chai")