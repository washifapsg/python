def perfectnumber(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if (sum==n):
        print("the number ",n,"is a perfect number")
    else:
        print("the number ",n,"is not a perfect number")
n=int(input("enter any number"))
perfectnumber(n)
