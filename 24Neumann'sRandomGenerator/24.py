
inputNum=int(input())
lineInput=input().split()
res=[]
for i in range (inputNum):
    count={}
    originNum=lineInput[i]
    count[originNum]=0
    while 1:
        i=0
        tempNum=int(originNum)*int(originNum)
        tempNum2=str(tempNum).zfill(8)
        middleNum=str(tempNum2)[2:6]
        if  middleNum in count:
            iterNum=len(count)
            break
        else:
            i=i+1
            count[middleNum]=i
            originNum=middleNum
    res.append(iterNum)
print(*res)

