def solution(t, p):
    answer = 0
    s=0
    e=len(p)
    while e<=len(t):
        sub=t[s:e]
        if int(sub)<=int(p):
            answer+=1
        s+=1
        e+=1
    return answer