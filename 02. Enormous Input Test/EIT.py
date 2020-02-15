
def EIT():
    u =int( input("Please enter the number of inpts"))
    k =int( input("Please enter the divider"))
    count =0
    for x in range(1,u+1):
        print ("PLease enter the no. {} number".format(x))
        o=int(input())
        if(o%k==0):
            count+=1
    return count

i = EIT()
print("{} integers are divisible over here".format(i))






