menu = ["vadapav", "bhaji", "samosa", "dosa"]

for index, item in enumerate(menu):
    print(f"index #{index} : {item}")

print("\n")

for index, item in enumerate(menu, start=2):
    print(f"index #{index} : {item}")
