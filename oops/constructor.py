class ChaiOrder:

    def __init__(self, chai_type, chai_amount):
        self.chai_type = chai_type
        self.chai_amount = chai_amount

    def print_detail(self):
        print(f"Chai type : {self.chai_type}, Chai amount : {self.chai_amount}")

order = ChaiOrder("Masala", 2)
order.print_detail()

order_2 = ChaiOrder("Ginger", 3)
order_2.print_detail()