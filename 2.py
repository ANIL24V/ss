n=int(input())
l1=[]
s=c=0
for i in range(0,n):
    l=list(map(int,input().split(' ')))
    l1.append(l)
for i in range(0,n):
    s=s+l1[i][i]
    c=c+l1[i][n-i-1]
if(s==c):
    print("yes")
else:
    print("no")
