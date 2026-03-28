def chai_customer():
    print("Welcome ! What chai would you like to have ?")
    order = yield
    while True:
        print(f"Preparing... {order} chai \n")
        order = yield

stall = chai_customer()
next(stall) # This is to start the generator

for i in range(10):
    stall.send(input("Enter your order : "))