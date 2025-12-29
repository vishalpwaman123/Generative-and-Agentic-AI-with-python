full_name = ("vishal", "prabhakar", "waman")

(first_name, middle_name, last_name) = full_name

print(f"Main character name : {first_name}, {middle_name}, {last_name}")

#################################

fname_ratio, lname_ratio = 2, 1

print(f"ratio is fname : {fname_ratio} and ratio is lname : {lname_ratio}")

fname_ratio, lname_ratio = lname_ratio, fname_ratio;

print(f"Swip ratio is fname : {fname_ratio} and ratio is lname : {lname_ratio}")

# membership

print(f"Is vishal in the full name ? { 'vishal' in full_name}") #'vishal' is case sensetive
print(f"Is rahul in the full name ? { 'rahul' in full_name}")