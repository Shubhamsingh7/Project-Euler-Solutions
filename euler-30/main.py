          
#euler 30

          
sumofnumber=0
for i in range(2,1000000):
    temp=i
    sum=0
    while(i!=0):
        
        digit=i%10
        sum+=(digit**5)
        i=i//10
    
    if temp==sum:
        sumofnumber+=sum
        print(sum)
        

print(sumofnumber)
    
    
    