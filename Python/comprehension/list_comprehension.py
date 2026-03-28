menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "iced" in tea.lower()]
tea_type = [tea for tea in menu if "tea" in tea.lower()]

print(iced_tea)
print(tea_type)


ages = [10, 11, 12, 13, 14, 15, 16]
young_age = [age for age in ages if age < 13]
print(young_age)

old_age = [age for age in ages if age >= 13]
print(old_age)