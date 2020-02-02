def prime_numbers_generation():
    yield 2
    yield 3
    yield 5 
    yield 7
    yield 11
    i=11
    while True:
        i+=2
        for j in range(3,int(i**0.5+1),2):
            if i%j==0:
                break 
        else:
            yield i
        
result=[]
answer=[]
a=prime_numbers_generation()
for z in range(200000):
    result.append(next(a))
lineinput=list(map(int,input().split()))
for a in lineinput:
    answer.append(result[a-1])
print(*answer)

 