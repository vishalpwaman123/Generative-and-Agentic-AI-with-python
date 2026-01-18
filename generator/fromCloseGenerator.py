def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
stall = full_menu()

for cup in stall:
    print(cup)
    
    
print("======== Closing the stall ========")


def chai_stall():
    try:
        while True:
            order = yield "Waiting for order...."
    except:
        print("Stall closed, No more chai available!")
        
stall = chai_stall()
print(next(stall))
stall.close()