def SmallFactorials():
    i = int(input("Please enter number of inputs please:-"))
    for x in range(1,i+1):
        print("Please enter number {} input:-".format(x))
        u=int(input())
        facto=1
        for g in range(1,u+1):
            facto=facto*g
        print("Small factorial for {} is {}".format(u,facto))


SmallFactorials()