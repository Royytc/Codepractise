numInput=input()
for i in range(int(numInput)):
    lineInput=input().split()
    a=int(lineInput[0])%6
    a=a+1
    b=int(lineInput[1])%6
    b=b+1
    print(a+b,end=" ")