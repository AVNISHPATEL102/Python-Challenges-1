def TheLeadGame():
    i = int(input("Please enter the number if scores you want to input"))
    p=1
    top=0
    winner = 1
    for x in range(1, i + 1):
        print("Please enter the {} match scores:- ".format(x))
        u = int(input())
        k = int(input())
        r=u-k
        if(r<0):
            r=r*(-1)
            p=2
        else:
            p=1
        if(r > top):
            winner = p
            top=r
    print("Your winner is {} with the highest lead {}".format(winner,top))


TheLeadGame()