num=int(input())
answer1=0
for i in range(num):
    s,a,b=list(map(int,input().split()))
    t=s/(a+b)
    answer1=t*a
    print(answer1,end=" ")
