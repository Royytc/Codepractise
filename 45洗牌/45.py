def swap_position(present_list,num_list,num):
    num=num % 52 
    present_list[num_list],present_list[num]=present_list[num],present_list[num_list]
def show_cards(num):
    ranks=['A', "2","3","4","5","6","7","8","9",'T','J','Q','K']
    suits=["C","D","H","S"]
    return suits[int(num/13)]+ranks[num%13]
origin=[x  for x in range(52)]
input_list=list(map(int,input().split()))
for loop in range(52):
    swap_position(origin,loop,input_list[loop])
for loop in range(52):
    answer=show_cards(origin[loop])
    print(answer,end=" ")
