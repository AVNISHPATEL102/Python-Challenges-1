def ReverseNumber():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number:- ".format(x))
        u = int(input())
        o=int(u**0.5)
        print("Your answer is {} ".format(o))


ReverseNumber()
