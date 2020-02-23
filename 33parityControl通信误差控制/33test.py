def parityCount(n):
        count=0
        while n!=0:
            n=n&(n-1)
            count+=1
        return count
num=map(int,list(input().split()))
result=[]
for i in num:
    answer=parityCount(i)
    result.append(answer)
print(*result)

