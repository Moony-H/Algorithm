def solution(friends, gifts):
    gPoint={f:0 for f in friends}
    gRecord={f:{i:0 for i in friends if i!=f} for f in friends} # 준것만 계산
    expect={f:0 for f in friends}
    for i in gifts:
        f,to=i.split()
        gPoint[f]+=1
        gPoint[to]-=1
        gRecord[f][to]+=1
        
    for a in friends:
        for b in friends:
            if a==b: continue
            if gRecord[a][b] == gRecord[b][a]:
                if gPoint[a]>gPoint[b]:
                    expect[a]+=1
                elif gPoint[a]<gPoint[b]:
                    expect[b]+=1
            elif gRecord[a][b]>gRecord[b][a]:
                expect[a]+=1
            else:
                expect[b]+=1
    answer=0
    for i in expect:
        answer=max(answer,expect[i])
    return answer/2