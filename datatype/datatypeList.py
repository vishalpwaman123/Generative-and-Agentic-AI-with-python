ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are : {ingredients}")
ingredients.remove("water")
print(f"Ingredients are : {ingredients}")

#############################################

spice_options = ["ginger", "cardamon"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"Chai : {chai_ingredients}")

##############################################

chai_ingredients.insert(2, "black tea")
print(f"Chai : {chai_ingredients}")

##############################################

last_element = chai_ingredients.pop()
print(f"Last element : {last_element}")
print(f"latest chai : {chai_ingredients}")

#############################################

chai_ingredients.reverse()
print(f"Chai reverse : {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai Sort : {chai_ingredients}")

#############################################

array_List = [1, 2, 3, 4, 5]
array_List.reverse()
print(f"array_List Reverse : {array_List}")
array_List.sort()
print(f"array_List Sort : {array_List}")
print(f"Print Max : {max(array_List)}")
print(f"print Min : {min(array_List)}")

#############################################

##### Operator Overloading and Byarray in python ##########

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor

print(f"Liquid mix : {full_liquid_mix}")

strong_brew = ["black tea"] * 3

print(f"Strong brew : {strong_brew}")