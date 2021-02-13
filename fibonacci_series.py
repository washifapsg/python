def fibonacci(n):
   if n==0:
       return 0;
   if n==1:
       return 1;
   else:
       return fibonacci(n-1)+fibonacci(n-2);
  
n=int(input("enter the limit of series"))
for i in range (0,n):
    a=fibonacci(i);
    print(a);
    
