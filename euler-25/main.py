import sys


fib_catch={}
def fib(a):
    if a in fib_catch:
        return fib_catch[a]
    elif a==1:
        value=1
    elif a==2:
        value=2
    else:
        value=fib(a-1)+fib(a-2)
        
    fib_catch[a]=value
    return value
    
  

for i in range(1,10000):
    count=0
    k=fib(i)
    while(k!=0):
        
        k=k//10
        count+=1
        if count==1000:
            print(i+1)
            print(fib(i))
            sys.exit()
