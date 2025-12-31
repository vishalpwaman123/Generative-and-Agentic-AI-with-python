chai_type = "plain"

def front_desk():

    def kitchen():
        global chai_type
        chai_type = "Irani"
    
    kitchen()

front_desk()
print(f"Final global chai : {chai_type}")