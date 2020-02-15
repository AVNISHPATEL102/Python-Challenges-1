def TurboSort():
    i = int(input("Please enter the number if inputs you want to test"))
    l=[]
    for x in range(1, i + 1):
        u = int(input())
        l.append(u)
    l.sort()
    print("The sorted array is then ")
    for x in l:
        print(x)


TurboSort()