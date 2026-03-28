#Pure vs Impure

def pure_chai(cups):    #RECOMMANDED
    return cups * 10

total_chai = 0

def impure_chai(cups):  #NOT RECOMMENDED
    global total_chai
    total_chai += cups


# Recuression function

def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(5))


# Lambda

# EXAMPLE 1

chai_type = ["masala", "kadak", "ginger", "green", "irani"]

filter_chai = list(filter(lambda x: x != "kadak", chai_type))

print(filter_chai)

# EXAMPLE 2

chai_price = [10, 15, 20, 25, 30, 35, 40]

filter_chai_price = list(filter(lambda x: x >15, chai_price))

print(filter_chai_price)