class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Milk or sugar is out od stock")
    print("Chai is ready")

make_chai(1, 0);
