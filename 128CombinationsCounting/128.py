def factorial(num):
    answer=1
    if num==0:
        return 1
    else:
        for i in range(1,num+1):
            answer*=i
        return answer
def combination_count(num1,num2):
    return factorial(num1)/(factorial(num2)*factorial(num1-num2))
num=input()
result=[]
for i in range(int(num)):
    num1,num2=map(int,list(input().split()))
    line_result=combination_count(num1,num2)
    result.append(int(line_result))
print(*result)

