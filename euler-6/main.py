
sum=0
sumOfsquare=0

for i in range(1,101):
    sumOfsquare+=i*i
    sum+=i
print(sum**2-sumOfsquare)