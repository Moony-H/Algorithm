def solution(sequence, k):
    answer = []
    for i in range(1,len(sequence)):
        sequence[i]+=sequence[i-1]
    L,R=(-1,0)
    results=[]
    while L<=R and R<len(sequence):
        result=sequence[R]-sequence[L] if(L!=-1) else sequence[R]
        if(result==k):
            results.append([L+1,R])
            R+=1
        elif(result>k):
            L+=1
        else:
            R+=1
    
    return sorted(results,key=lambda x:(x[1]-x[0],x[0]))[0]