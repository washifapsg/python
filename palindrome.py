def rev(n):
    
    rev_n=0
    while(n>0):
        rev_n=int (rev_n*10+n%10)
        n=int(n/10)
       
    return rev_n


x=int(input("enter the value to check palindrome"))
y=rev(x)

if(x==y):
    print("given value is palindrome")
else:
    print("given value is not palindrome") 
