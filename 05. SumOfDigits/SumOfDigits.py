def SumOfDigits():
    i = int(input("Please enter the number if inputs you want to test"))
    for x in range(1,i+1):
        print("Please enter the {} input:- ".format(x))
        u = int(input())
        total=0;
        while u>0:
            total= total + (u%10)
            u=int(u/10)
        print("The sum of digits over here is {} ".format(total))

SumOfDigits()