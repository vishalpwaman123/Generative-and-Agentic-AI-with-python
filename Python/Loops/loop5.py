for item in range(1, 6):
    if not item % 2:
        continue
    else:
        if item == 3:
            break
        print(f"{item} is odd")


#######################################################################


flavours = ["Ginger", "Out of stock", "Lemon", "Discountinue", "Tulsi"]

for item in flavours:
    if item.lower() == "out of stock":
        continue
    elif item.lower() == "discountinue":
        break
    print(f"{item}")


#########################################################################


staff = [("vishal", 16), ("rahul", 17), ("prabhakar", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")