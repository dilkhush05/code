class student:
    collage_name = "JIS Collage Of Engineering" #class attrebutes

    def __init__(self , name , marks):
        self.name = name     #obj attrebute
        self.marks= marks

        print("adding new students in databases")

S1 = student("arjum", 95.5)
print(S1.name , S1.marks)
print(S1.collage_name)

S2 = student("radhe", 97.5)
print(S2.name , S2.marks)
print(student.collage_name)