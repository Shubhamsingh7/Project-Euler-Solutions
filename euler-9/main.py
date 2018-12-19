# euler 9

import sys

for i in range(1,1000):
    for j in range(1,i):
        for k in range(1,j):
            if i+j+k==1000 and k**2 + j**2 == i**2:
                r = i*j*k
                print(" sghghgh {} {} {}".format(j,k,i))
                print(r)
                sys.exit()
            
            
        


