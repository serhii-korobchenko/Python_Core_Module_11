class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, value):
        return self.add_value + value


two_adder = Adder(2)
print(two_adder(5))  # 7
print(two_adder(4))  # 6

three_adder = Adder(3)
print(three_adder(5))  # 8
print(three_adder(4))  # 7