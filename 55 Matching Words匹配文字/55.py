def match_words(input) :
    result=[]
    store=[]
    for i in input:
        if i not in store:
            store.append(i)
        else:
            if i not in result:
                result.append(i)  
    result.sort()
    return result
input=list(map(str,input().split()))
a = match_words(input)
print(*a)