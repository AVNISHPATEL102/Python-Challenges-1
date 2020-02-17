def ReverseNumber():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number:- ".format(x))
        u = int(input())
        o=1
        t=""
        while(u>0):
            t+=(str)(u%10)
            o=o*10
            u=int(u/10)
        print("Your answer is {} ".format(t))


ReverseNumber()
