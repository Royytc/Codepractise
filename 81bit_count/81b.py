def count_bits(x):
    c=0
    for i in range(32):
        c += (x & 1)
        x >>= 1
    return c
num=input()
list_input=list(map(int,input().split()))
result=[]
count=0
for i in list_input:
    if i<0:
        i=2**32+i
        count=count_bits(i) 
    else:
        count=count_bits(i)  
    result.append(count)
print(*result)