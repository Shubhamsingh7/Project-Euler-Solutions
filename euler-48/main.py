

sum=0
for i in range(1,1001):
    sum+=i**i
    
print(sum)
num=[]
count=0
while sum!=0:
    num.append(sum%10)
    sum=sum//10
    count+=1
    if count==10:
        num.reverse()
        
        print(num)
        break