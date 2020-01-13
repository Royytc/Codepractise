def only_brackets(str):
    aim_list=["(",")","[","]","{","}","<",">"]
    str_list=list(str)
    result_list=[]
    for i in str_list :
        if i in aim_list:
            result_list.append(i)
    return "".join(result_list)
def is_valid(str):
    stack=[]
    parent_map={")":"(","]":"[","}":"{",">":"<"}
    for c in str:
        if c not in parent_map:
            stack.append(c)
        elif not stack or parent_map[c] !=stack.pop():
            return 0
    return not stack
num=input()
result=[]
for i in range(int(num)):
    lineinput=input()
    onlyBrackets=only_brackets(lineinput)
    answer=is_valid(onlyBrackets)
    result.append(int(answer))
print(*result)



