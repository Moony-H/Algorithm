from collections import defaultdict
    


def solution(gems):
    answer=[]
    kind=list(set(gems))
    kind_len=len(kind)
    start=0
    end=0
    check=defaultdict(int)
    check[gems[0]]
    check[gems[0]]+=1
    
    answer=[0,len(gems)-1]
    while end<len(gems) and start<len(gems):
        if kind_len!=len(check):
            end+=1
            if end==len(gems):
                break
            check[gems[end]]
            check[gems[end]]+=1
        else:
            if answer[1]-answer[0]>end-start:
                answer[0]=start
                answer[1]=end
            check[gems[start]]-=1
            if check[gems[start]]==0:
                del check[gems[start]]
            start+=1
            
            
        
    answer[0]+=1
    answer[1]+=1
    return answer