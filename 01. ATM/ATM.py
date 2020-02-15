def ATM(a,b):
    if(a<(b+0.5)  and a%5==0 ):
        print(b-a-0.5)
    else:
        print(b)




a = int(input("Please enter the amount of money you want to withdraw"))
b = int(input("Please enter the amount of money you have in your account"))


ATM(a,b)