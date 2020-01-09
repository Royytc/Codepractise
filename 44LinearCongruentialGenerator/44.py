num=int(input())
res=[]
for i in range(num):
    line_input=list(map(int,input().split()))
    answer=line_input[3]
    for j in range(line_input[4]):
        answer=(line_input[0]*answer+line_input[1])%line_input[2]
    res.append(answer)
print(*res)    

