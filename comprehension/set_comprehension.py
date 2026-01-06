favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais } # Create Set with unique value

print(unique_chai)


recipes = {
    "Masala Chai" : ["ginger", "cardamom", "clove"],
    "Elaichi Chai" : ["cardamom", "milk"],
    "Spicy Chai" : ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredient in recipes.values() for spice in ingredient} 

print(unique_spices)