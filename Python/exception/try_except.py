chai_menu = { "Masala": 30, "Ginger": 40 }

# chai_menu["Lemon"] # cause Key Error

try:
    chai_menu["Lemon"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("Hello chai order", chai_menu)