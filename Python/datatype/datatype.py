sugar_amount = 2
print(f"Initial Value : {sugar_amount}")
sugar_amount = 12
print(f"Second value : {sugar_amount}")

print(f"ID of 2 : {id(2)}") 
print(f"ID of 12 : {id(12)}")

#Output

#ID of 2 : 140716595651736
#ID of 12 : 140716595652056

# 2 and 12 stored at different location means same location or reference not change value
# this is also know as immutable

spice_mix = set()
print(f"Initial spice mix id : {id(spice_mix)}")
print(f"Initial spice mix id : {spice_mix}")
spice_mix.add("Onian")
spice_mix.add("ladyfinger")
spice_mix.add("lemon")
print(f"After spice mix id : {spice_mix}")
print(f"After spice mix id : {id(spice_mix)}")

#Output
#Initial spice mix id : 1668858791968
#Initial spice mix id : set()
#After spice mix id : {'lemon', 'ladyfinger', 'Onian'}
#After spice mix id : 1668858791968

#Intial and after refernce is same only change the value in same reference
# this is called as mutable