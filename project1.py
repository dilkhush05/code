import random

target = random.randint(2,20)

while True:
    userchoise = input("guss the target or quit : ")
    if(userchoise == "q"):
       # print(target)
        break

    userchoise = int(userchoise)

    if (userchoise == target):
        print("success : cottect guss!! ._.)__",target)
        break
    elif (userchoise < target) :
        print("your number was to small . try again : ")
    else :
        print("your number was to big . try again :")

print("____GAME~OVER____")
