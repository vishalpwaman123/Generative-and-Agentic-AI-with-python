class ChaiOrder:

    def __init__(self, chai_type, sweetness, size):
        self.chai_type = chai_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data): #cls is class reference as by default parameter
        return cls(order_data["chai_type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string): #cls is class reference as by defaukt parameter
        chai_type, sweetness, size = order_string.split("-")
        return cls(chai_type, sweetness, size)


class ChaiUtils:

    @staticmethod
    def is_Valid_Size(size):
        return size.upper() in ["SMALL", "MEDIUM", "LARGE"]

print("Is size valid? : ", ChaiUtils.is_Valid_Size("small"))

order1 = ChaiOrder.from_dict({"chai_type": "Masala", "sweetness":"Medium", "size":"Large"})
print(order1.__dict__)

order2 = ChaiOrder.from_string("Ginger-Low-Small")
print(order2.__dict__)

order3 = ChaiOrder("Gud", "Medium", "Large")
print(order3.__dict__)