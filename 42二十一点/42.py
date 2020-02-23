def pointscore (a:list):
    playing_cards={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10}
    score=0
    have_A=0
    for i in a:
        score+=int(playing_cards[i])
        if i=='A':
            have_A=1
    if score>21:
        return "Bust"
    else:
        if have_A==1 and score+10<=21:
            score+=10
        return score
result=[]
for i in range(int(input())):
    input_line=list(input().split())
    answer=pointscore(input_line)
    result.append(answer)
print(*result)



