def serve_chai():
    yield "Cup 1 : Masala chai"
    yield "Cup 2 : Ginger chai"
    yield "Cup 3 : Elaichi Chai"
    
stall = serve_chai()

# for cup in stall:
#     print(cup)

print(next(stall))
print(next(stall))
print(next(stall))

print("=============")

def serve_chai_types():
    return ["Cup_1 : Masala chai", "Cup_2 : Ginger chai", "Cup_3 : Elaichi Chai"]

for cup in serve_chai_types():
    print(cup)