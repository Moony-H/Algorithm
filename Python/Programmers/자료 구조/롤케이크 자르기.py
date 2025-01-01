

def solution(topping):
    answer = 0
    big={}
    small={}
    for i in topping:
        small[i]=small.get(i,0)+1
    for i in topping:
        big[i]=big.get(i,0)+1
        small[i]-=1
        if small[i]==0:
            small.pop(i)
        if len(big)==len(small):
            answer+=1
    return answer