def PackingCupcakes():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number:- ".format(x))
        u = int(input())
        t=0
        r=0
        for v in range(1,u+1):
            if(u%v > r ):
                t = v
                r=u%v
        print("Your answer is {} ".format(t))


PackingCupcakes()

