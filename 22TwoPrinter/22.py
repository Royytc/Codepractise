from math import ceil
def TwoPrinter(sec_A,sec_B,num_page):
    page_need_a=ceil(num_page*sec_B/(sec_B+sec_A))
    page_need_b=ceil(num_page*sec_A/(sec_B+sec_A))
    if page_need_a*sec_A<=page_need_b*sec_B:
       return page_need_a*sec_A
    else:
         return page_need_b*sec_B
num=input()
result=[]
for i in range(int(num)):
    sec_A,sec_B,num_page=map(int,list(input().split()))
    result.append(TwoPrinter(sec_A,sec_B,num_page))  
print(*result)  
