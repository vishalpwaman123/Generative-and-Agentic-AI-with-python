class BaseChai:

    def __init__(self, chai_type):
        self.type = chai_type

    def prepare(self):
        print(f"Preparing {self.type} chai")

class MasalaChai(BaseChai):

    def add_spices(self):
        print(f"Adding cardamom, ginger and cloves.")

class ChaiShop:
    chai_cls = BaseChai 

    def __init__(self):
        self.chai = self.chai_cls("Regular") #chai is object of BaseChai class

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop.")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

shop = ChaiShop()
shop.serve()

fancy_shop = FancyChaiShop()
fancy_shop.serve()

fancy_shop.chai.add_spices()