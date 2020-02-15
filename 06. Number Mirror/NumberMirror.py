def NumberMirror():
    i = int(input("Please enter the number if inputs you want to test"))
    for x in range(1,i+1):
        print("Please enter the {} input:- ".format(x))
        u = int(input())
        print("The numebr entered is {}".format(u))


NumberMirror()