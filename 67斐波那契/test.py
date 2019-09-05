arr=[1]*256
arr[0]=1
arr[1]=0
for i in range(2,10):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[9])
