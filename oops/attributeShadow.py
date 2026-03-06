class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()

print(f"Before Chaning temperature : {cutting.temperature}")

cutting.temperature = "Cold"

print(f"After Chaning temperature : {cutting.temperature}")

print(f"Direct access temperature : {Chai.temperature}")

del cutting.temperature

print(f"After deleting temperature : {cutting.temperature}")

cutting.is_Hot = True

print(f"Object cutting is Hot : {cutting.is_Hot}")

del cutting.is_Hot

print(f"Object cutting is Hot : {cutting.is_Hot}")