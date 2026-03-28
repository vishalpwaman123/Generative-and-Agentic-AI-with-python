def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type  #nonlocal help you to use parent variable in local function
        chai_type = "kesar"
    
    kitchen()
    print(f"After kitchen update, chai type is {chai_type}")

update_order()