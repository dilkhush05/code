class complex:
    def __init__(self, real , img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i +", self.img ,"j")
#addition two complex number
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)
#substract of two complex number
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex( newReal, newImg)

num1=complex(1,3)
num1.showNumber()

num2=complex(5,7)
num2.showNumber()

num3 = num1+num2
num3.showNumber()

num3 = num1-num2
print("subtract is :" ,num3.showNumber())
