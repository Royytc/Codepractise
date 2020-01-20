def Rock_Paper_Scissors(input:list):
    first_score=0
    second_score=0
    first_win=['RS','SP','PR']
    second_win=['SR','PS','RP']
    for i in input:
        if i in first_win:
            first_score +=1
        if i in second_win:
            second_score+=1
    if first_score > second_score:
        return 1
    else:
        return 2
num=input()
result=[]
answer=0
for i in range(int(num)):
    input_list=list(map(str,input().split()))
    answer=Rock_Paper_Scissors(input_list)
    result.append(answer)
print(*result)

        