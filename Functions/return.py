# EXAMPLE IF RETURN NOTHING

def make_chai():
    #return "Here is your masala chai"
    print("Here is your masala chai")

print(make_chai()) # RETURN None

######################## EXAMPLE 2 ( RETURN VALUE ) #######################

def chai_Status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    else:
        return "Chai is ready"

print(chai_Status(0))
print(chai_Status(1))

###################### EXAMPLE 3 ( RETURN MULTIPLE VALUE ) ################

def chai_report():
    return 100, 20, 30 # SOLD, REMAINING

sold, remaining, _ = chai_report()
print("SOLD : ", sold, "REMAINING : ",remaining)