
import sys

for i in range(20,99999999999):
    for j in range(1,21):
        if i%j==0:
            if j==20:
                print(i)
                sys.exit()
        else:
            break