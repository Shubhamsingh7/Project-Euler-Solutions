
#euler 20
def fact(n):
    
    if n==1:
        value=1
    else:
        value= n*fact(n-1)
    
    return value 
sum=0   

k=fact(100)
while(k!=0):
    sum+=k%10
    k=k//10
print(sum)
