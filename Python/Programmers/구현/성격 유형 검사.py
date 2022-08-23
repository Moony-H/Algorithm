def solution(survey, choices):
    answer = ''
    points=[3,2,1,0,1,2,3]
    type=['RT','CF','JM','AN']
    d={}
    for i,num in enumerate(choices):
        index=1
        if(num<=3):
            index=0
        d[survey[i][index]]=d.get(survey[i][index],0)+points[num-1]
    
    for i in type:
        first=i[0]
        sec=i[1]
        if(d.get(first,0)>=d.get(sec,0)):
            answer+=first
        else:
            answer+=sec
    
    return answer