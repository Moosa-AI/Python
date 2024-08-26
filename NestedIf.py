num=int(input("Number: "))
if (num<0):
    print("Number is negative")
elif(num>0):
    print("Number is positive".capitalize())
    if(num<=10):
        print("number is between 0-10".capitalize())
    elif (num>10 and num<20):
        print("number  is between 11 and 19")
    else:
        print("Number is greater than 10")
else:
    print("number is zero")