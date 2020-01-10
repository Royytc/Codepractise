def  josephusproblem(num,k):
    link =[x+1 for x in range(num)]
    ind = 0
    for loop in range(num- 1) :
        ind = (ind - 1 + k)% len(link)
        del link[ind]
    print (link[0])
    
num,k=list(map(int,input().split()))
josephusproblem(num,k)
    



            
     

