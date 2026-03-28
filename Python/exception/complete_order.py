def InvalidChaiError(Exception): pass

def bill(flavour, cups):
    menu = {"Masala": 30, "Ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("That chai is not in available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be in integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai is {total} rupees")
    except Exception as e: 
        print("Error : ", e)
    finally:
        print("Thank you for visiting our chai shop")

bill("mint", 2)
bill("Masala", "two")
bill("Masala", 2)