def AddTwoNumbers():
    i = int(input("Please enter the number of inputs you are going to enter:- "))
    for x in range(1,i+1):
        print("Please enter two integers")
        i1 = int(input())
        i2 = int(input())
        total=i1+i2
        print("Total = {}".format(total))



AddTwoNumbers()