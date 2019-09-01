inputNum=int(input())
lineInput=input().split()
res=[]
for i in range (inputNum):
    count={}
    originNum=lineInput[i]
    count[originNum]=0
    while 1:
        i=0
        tempNum=int（originNum)*int（originNum)
        middleNum=str(tempNum)[3:7]
        if  middleNum in count:
            iterNum=len(count)-count[middleNum]-1
            break
        else:
            i=i+1
            count[middleNum]=i
            originNum=middleNum
    res.append(iterNum)
    print(*res)

