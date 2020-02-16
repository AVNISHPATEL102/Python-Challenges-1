def FirstLastDigit():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number:- ".format(x))
        u = int(input())
        l = u % 10
        while(u >= 100):
            u=u/10
        f=int(u/10)
        t=f+l
        print("Your answer is {} ".format(t))


FirstLastDigit()


