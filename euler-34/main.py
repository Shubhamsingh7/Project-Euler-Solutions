# Sum of curious number



def fact(n):
    pro=1
    for i in range(n,0,-1):
        pro*=i
    return pro
    


def curious(n):
    sum=0
    total=0
    for i in list(str(n)):
        i=int(i)
        sum+=fact(i)
    if n==sum:
        total+=sum
        print(n)
    return total
        
    
        
        


total=0
for i in range(3,100000):
    result=curious(i)
    total+=result
    
    

print(total)

