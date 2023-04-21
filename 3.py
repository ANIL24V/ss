'''
a=int(input())
b=int(input())
while(1):
    r=b%a
    if(r==0):
        print(a)
        break
    else:
        b=a
        a=r'''

l=list(map(int,input().split()))
def gcd():
    a=l[0]
    b=l[1]
    while(a!=0):
        r=b%a
        if(r==0):
            l.remove(l[0])
            l.remove(l[1])
            l.insert(0,a)
            return a
        else:
            b=a
            a=r
for i in range(0,len(l)-1):
    c=gcd()
    print(c)
    





