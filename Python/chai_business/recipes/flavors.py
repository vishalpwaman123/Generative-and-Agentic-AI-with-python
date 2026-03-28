from utils.discounts import discount_calculation

DISCOUNT = 0.1
ELACHAI_CHAI_PRICE = 10
GINGER_CHAI_PRICE = 15

def elachai_chai():
    return "Elachai chai is ready"

def ginger_chai():
    return "Ginger chai is ready"

def invalid_chai_type(chai_type):
    return f"{chai_type} no available"

def chai_order(CHAI_TYPE, TOTAL_CHAI):

    if CHAI_TYPE == "ELACHAI_CHAI":
        return elachai_chai(), discount_calculation(TOTAL_CHAI, ELACHAI_CHAI_PRICE, DISCOUNT)
    elif CHAI_TYPE == "GINGER_CHAI":
        return ginger_chai(), discount_calculation(TOTAL_CHAI, GINGER_CHAI_PRICE, DISCOUNT)
    else:
        return invalid_chai_type(), 0