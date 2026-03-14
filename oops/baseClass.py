class Chai:
    
    def __init__(self, chai_type, chai_amount):
        self.chai_type = chai_type
        self.chai_amount = chai_amount

    def print_chai_detail(self):
        print(f"Chai : {self.chai_type}, amount : {self.chai_amount}")

# Example 1

# class GingerChai(Chai):

#     def __init__(self, chai_type, chai_amount, spice_level):
#         self.chai_type = chai_type
#         self.chai_amount = chai_amount
#         self.spice_level = spice_level

# Example 2

# class GingerChai(Chai):

#     def __init__(self, chai_type, chai_amount, spice_level):
#         Chai.__init__(self, chai_type, chai_amount)
#         self.spice_level = spice_level



class GingerChai(Chai):

    def __init__(self, chai_type, chai_amount, spice_level):
        super().__init__(chai_type, chai_amount)
        self.spice_level = spice_level

ginger_Chai = GingerChai("Ginger", 1, "More")
ginger_Chai.print_chai_detail();