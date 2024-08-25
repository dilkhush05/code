class student:

    def __init__(self, name ,marks):

        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hii",self.name,"yur avrage marks is ",sum/3)

S1 = student("arjum",[12,25,75,63])
S1.get_avg()



