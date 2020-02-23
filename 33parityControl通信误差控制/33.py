def parityCount(n):
        count=0
        while n!=0:
            n=n&(n-1)
            count+=1
        return count

def  symbol_return(n):    
        if n>128:
            return chr(n-128)
        else :
            return chr(n)
result=[]
line_input=map(int,list(input().split()))
for i in line_input:
    if parityCount(i)%2 == 0:
        result.append(symbol_return(i))
print("".join(i for i in result))
