a=600851475143

def prime(n):
    flag=0
    for i in range(2,n//2):
        if n%i==0:
            flag=1
        else:
            pass
    if flag==1:
        return False
    else:
        return True
        


primenum=0
for i in range(2,a//2):
    if a%i==0:
        k=prime(i)
        if k==True:
            primenum=i
            print("primenum={}".format(primenum))
    else:
        pass



print(primenum)            