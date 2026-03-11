class ChaiCup:
    size = 10

    def describe(self):
        return f"This is a {self.size} ml chai cup";

# Example 1
cup = ChaiCup()
print(cup.describe())

# Example 2
print(ChaiCup.describe(cup))

# Example 3
cup_Chai = ChaiCup()
cup_Chai.size = 15
print(cup_Chai.describe())