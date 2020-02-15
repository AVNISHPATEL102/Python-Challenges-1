def FindRemainder():
    i = int(input("Please enter the number if inputs you want to test"))
    for x in range(1, i + 1):
        print("Please enter the {} input:- ".format(x))
        u = int(input())
        k = int(input())
        r=u%k
        print("Your remainder is {}".format(r))


FindRemainder()