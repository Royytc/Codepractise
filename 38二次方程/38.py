def quadratic_equation(a,b,c):
    imaginary_part=(abs(b*b-4*a*c)**0.5)/(2*a)
    real_part=-b/(2*a)
    if b*b-4*a*c<0:
        return str(int(real_part))+"+"+str(int(imaginary_part))+"i  "+str(int(real_part))+"-"+str(int(imaginary_part))+"i;"
    else:
        return str(int(real_part+imaginary_part))+" "+str(int(real_part-imaginary_part))+";"
        
num=input()
result=[]
for i in range(int(num)):
    a,b,c=map(int,list(input().split()))
    out_str=quadratic_equation(a,b,c)
    result.append(out_str)
print(*result)