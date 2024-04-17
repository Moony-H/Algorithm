def solution(storey):
    answer = 0
    storey=list(reversed(list(map(int,list(str(storey))))))
    storey.append(0)
    for i in range(len(storey)):
        if len(storey)-1==i and storey[i]==0:
            break
        if storey[i]>=6:
            answer+=10-storey[i]
            storey[i+1]+=1
        elif storey[i]==5:
            if storey[i+1]>=5:
                answer+=10-storey[i]
                storey[i+1]+=1
            else:
                answer+=storey[i]
        else:
            answer+=storey[i]
    return answer