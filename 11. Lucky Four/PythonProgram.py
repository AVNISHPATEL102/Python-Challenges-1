def LuckyFour():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number:- ".format(x))
        u = int(input())
        count=0
        while(u >0):
            t=u%10
            if(t==4):
                count=count+1
            u=int(u/10)
        print("Your answer is {} ".format(count))


LuckyFour()

