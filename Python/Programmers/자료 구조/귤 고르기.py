def solution(k, tangerine):
    answer=0
    orangeHash={}
    for i in tangerine:
        orangeHash[i]=orangeHash.get(i,0)+1
    orange=sorted(orangeHash.values(),reverse=True)
    sums=0
    for i,amount in enumerate(orange):
        sums+=amount
        if sums>= k:
            return i+1
    return len(orange)