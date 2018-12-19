

#project Euler 2nd question


fib_catch={}

def fib(a):
    if a in fib_catch:
        return fib_catch[a]
    elif a==1:
        value= 1
    elif a==2:
        value= 2
    else:
        value= fib(a-1)+fib(a-2)
    
    fib_catch[a]=value
    return value
    
    
sum=0
for i in range(1,1000):    
    result=fib(i)
    if result >4000000:
        break
    if result%2==0:
        sum+=result
print(sum)
