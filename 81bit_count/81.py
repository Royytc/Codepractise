def intToBin32(i):
    return (bin(((1 << 32) - 1) & i)[2:]).rjust(32)
def count_1(n):
    count=0
    while n != 0:
        n=n&(n-1)
        count+=1
    return count
def count_1A(n):
    count=0
    while n!=0:
        if n%2:
            count+=1
            n=n>>1
    return count
num=input()
list_input=list(map(int,input().split()))
result=[]
for i in list_input:
    bin_num=intToBin32(i)
    count=0
    for j in range(32):
        if bin_num[j]=="1":
            count+=1
    result.append(count)
print(*result)





