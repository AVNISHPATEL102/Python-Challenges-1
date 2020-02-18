def Servant():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number of pairs:- ".format(x))
        u = int(input())
        if(u<10):
            print("What an obedient servant you are!")
        else:
            print("-1")



Servant()