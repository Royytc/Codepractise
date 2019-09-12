num=int(input())
for i in range(num):
    s,r,p=list(map(int,input().split()))
    count=0
    while  s<r:
        s=s*(1+p/100)
        count+=1
    print(count,end=" ")
