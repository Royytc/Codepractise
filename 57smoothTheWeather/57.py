num=int(input())
result=[]
inputNum=[]
inputNum=list(map(float,input().split()))
for i in range(num):
    if i==0 or i==num-1:
        result.append(inputNum[i])
    else:
        result.append(((inputNum[i-1]+inputNum[i]+inputNum[i+1])/3))
print(*result)