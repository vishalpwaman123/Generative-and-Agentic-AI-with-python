class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_Hot = True;
print(Chai.is_Hot)

#Creating New object

masala = Chai()
print(masala.origin)
print(masala.is_Hot)

masala.is_Hot = False;

print("Class Chai is Hot : ", Chai.is_Hot)
print("Object Chai is Hot : ", masala.is_Hot)
