def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print(f"Sorry Chai is not in menu")
    except TypeError:
        print(f"Quantity must be in number")


process_order("lemon", 2)
process_order("masala", "two")