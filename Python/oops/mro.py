# MRO - Method resolution Order ( Multiple Inheritance )

class A:
    label = "Class A Label"

class B(A):
    label = "Class B label"

class C(A):
    label = "Class C label"

class D(B, C): # priority goes to first inherit class
    pass


print(D.label) # Print "Class B label" Becasuse B inherit first 