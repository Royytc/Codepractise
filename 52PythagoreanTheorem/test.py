men=[1,1]
for  i in range(2,8):
    men.append(men[i-1]+men[i-2])
print(men)