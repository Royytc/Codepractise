def bulls_cows(k:str,input_number:str):
    count1=0
    count2=0
    for i in  range(len(k)):
        if k[i]==input_number[i]:
            count1+=1
        if input_number[i] in k:
            count2+=1
    return "%d-%d"%(count1,count2-count1)
k,num=input().split()
input=list(input().split())
result=[]
for input_number in input:
    result.append(bulls_cows(k,input_number))
print(*result)



    
