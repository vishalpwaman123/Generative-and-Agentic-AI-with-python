first_name = "Vishal"
last_name = "Waman"

print(f"First name : {first_name} & Last name : {last_name}")

full_name = "Vishal Prabhakar Waman"

print(f"case 1 : {full_name[0:5]}") # Visha
print(f"case 2 : {full_name[:5]}") # Visha
print(f"case 3 : {full_name[7:]}") # Prabhakar Waman
print(f"case 4 : {full_name[::-1]}") #namaW rakahbarP lahsiV -- Reverse string

encoded_string = full_name.encode("utf-8")
print(f"Encoded label : {encoded_string}")
decoded_string = encoded_string.decode("utf-8")
print(f"Decoded label : {decoded_string}")