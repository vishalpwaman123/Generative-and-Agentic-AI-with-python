full_name = {"vishal", "prabhakar", "waman"}
father_name = {"prabhakar", "bapurao", "waman"}

union_name = full_name | father_name
print(f"Union of name : {union_name}")

intersection_name = full_name & father_name
print(f"Intersection of name : {intersection_name}")

only_in_full_name = full_name - father_name
print(f"Only in full name : {only_in_full_name}")

print(f"bapurao in father name ? {'bapurao' in father_name}")