from  collections  import deque
def  josephusproblem(num,k):
    link =deque(x+1 for x in range(num))
    for loop in range(num- 1) :
        link.rotate(-k+1)
        link.popleft()
    print (link[0])    
num,k=list(map(int,input().split()))
josephusproblem(num,k)