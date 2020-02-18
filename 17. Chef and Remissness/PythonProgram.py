def ChefAndRemissness():
    i = int(input("Please enter the number if input you want to calculate"))
    for x in range(1, i + 1):
        print("Please enter the {} number of pairs:- ".format(x))
        u = int(input())
        n=  int(input())
        tlist = [u,n]
        tlist.sort()
        print("Your answer is {}  {} ".format(tlist[1],tlist[1]*2))


ChefAndRemissness()