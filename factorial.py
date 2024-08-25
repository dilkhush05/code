
def factroial(x):
    i = 1
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact





x = int(input("factorial of :" ))
fact = factroial(x)
print  (fact)

#using recursion:-
def factroial(x):
    if(x == 0 or x == 1):
        return 1



    fact = factroial(x-1)*x
    return fact





x = int(input("factorial of :" ))
fact = factroial(x)
print  (fact)