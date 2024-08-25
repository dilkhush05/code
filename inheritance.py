class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class tyotacar(car):
    def __init__(self, brand):
        self.brand = brand

class fortuner(tyotacar):
    def __init__(self, type):
        self.type = type
        print(self.type)
car1 = fortuner("petrol..")

car.start()

