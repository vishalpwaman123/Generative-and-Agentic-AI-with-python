# EXAMPLE 1

chai = "Ginger chai"

def prepare_chai(order):
    print("Preparing : ",order)

prepare_chai(chai)
print(chai)

######################### EXAMPLE 2 ########################

chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42 # [1, 42, 3]

edit_chai(chai)
print(chai)

######################### EXAMPLE 3 #########################

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #POSITIONAL
make_chai(tea="Green", sugar="Medium", milk="No")


####################### EXAMPLE 4 ###########################

def special_chai(*ingredients, **extras):
    print("Ingredients : ", ingredients)
    print("Extra : ",extras)

special_chai("Masala", "Irani", sweetener="Honey", form="yes")


###################### EXAMPLE 5 ###########################

def chai_order(order=[]):
    order.append("Masala")
    print(order)

chai_order()
chai_order()

###################### EXAMPLE 6 ##########################

def chai_orders(order = None):
    if order is None:
        order=[]
    
    print(order)

chai_orders()
chai_orders()

####################### END ########################