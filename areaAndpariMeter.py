class circle:
    def __init__(self,redius):
        self.redius = redius

    def area(self):
        return 3.14 * self.redius ** 2

    def parimeter(self):
        return 3.14 * self.redius * 2

c1 = circle(21)
print("area is :",c1.area())
print("parimeter is :",c1.parimeter())