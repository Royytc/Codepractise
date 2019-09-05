def fib(num):
    if num<=1:
        return num
    a=0
    b=1
    for i in range(num):
        a,b=b,a+b
    return a 

numInput=input()
for i in range(int(numInput)):
    lineInput=input()
    n=0
    while int(lineInput)>int(fib(n)):
        n=n+1
    print(n,end=" ")