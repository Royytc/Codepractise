num=input()
for i in range(int(num)):
    a,b,c=map(int,input().split(" "))
    if a*a+b*b==c*c:
        print("R",end=" ")
    if a*a+b*b>c*c:
        print("A",end=" ")
    if a*a+b*b<c*c:
        print("O",end=" ")
