def openBox(cards,start):
    result=0
    while cards[start]!=-1:
        temp=cards[start]
        cards[start]=-1
        start=temp
        result+=1
    return result


def solution(cards):
    answer = 0
    cards=[i-1 for i in cards]
    for i in range(len(cards)):
        tempCards=cards.copy()
        result1=openBox(tempCards,i)
        for j in range(len(cards)):
            temp2Cards=tempCards.copy()
            if tempCards[j]==-1:
                continue
            result2=openBox(temp2Cards,j)
            answer=max(answer,result1*result2)
    return answer