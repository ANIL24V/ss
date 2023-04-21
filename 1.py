import math
n=int(input())
while(1):

    a=n**2
    d=int(math.log(n,10))+1
    b=a%(10**d)
    if(n==b):
        print(n,"is orthomorphic num")
        break
    else:
        n=n+1
