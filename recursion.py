def calculat(x):
    if(x == 0):
        return 0
    sum = calculat(x-1) + x
    return sum

x = int (input("your input :"))
sum = calculat(x)
print ( sum)