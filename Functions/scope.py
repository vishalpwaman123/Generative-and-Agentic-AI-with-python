def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner : {chai_order}")
    
    print_order()
    print(f"Outer : {chai_order}")

chai_order = "Tulsi" # Global scope
chai_counter()
print(f"Global : {chai_order}")