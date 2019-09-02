def fib(num):
    if num==0 or num==1:
        return num
    return int(fib(num-1))+int(fib(num-2))
numInput=input()
for i in range(int(numInput)):
    lineInput=input()
    n=0
    while int(lineInput)>int(fib(n)):
        n=n+1
    print(n,end=" ")

