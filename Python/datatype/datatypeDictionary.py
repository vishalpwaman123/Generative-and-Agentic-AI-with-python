full_name = dict(fname="vishal", mname="prabhakar", lname="waman")
print(f"Full name : {full_name}")

#######################################

family_name = {}
family_name["son"] = "vishal"
family_name["wife"] = "kajal"

print(f"Family son name : {family_name["son"]}")
print(f"Family name : {family_name}")

del family_name["son"]

print(f"Family name : {family_name}")

print(f"is mname in full name ? {'mname' in full_name}")

########################################

chai_order = {"type":"Ginger chai", "size":"medium", "Sugar":1}

print(f"Order details (keys) : {chai_order.keys()}")
print(f"order details (values) : {chai_order.values()}")
print(f"Order details (items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"removed last item : {last_item}")

########################################

extra_spices = {"cardamon":"crushed", "ginger":"sliced"}
chai_order.update(extra_spices)
print(f"Updated chai receipe : {chai_order}")

########################################

name_note = full_name.get("fname", "No first name")
print(f"name note is : {name_note}")

name_note = full_name.get("grfname", "No grand father name")
print(f"name note is : {name_note}")