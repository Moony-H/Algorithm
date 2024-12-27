def solution(bridge_length, weight, truck_weights):
    answer = 0
    q=[0 for _ in range(bridge_length)]
    i=0
    allWeight=sum(truck_weights)
    done=0
    nowW=0
    while done<allWeight:
        answer+=1
        front=q.pop(0)
        nowW-=front
        done+=front
        if i>=len(truck_weights):
            q.append(0)
            continue
        if nowW+truck_weights[i]>weight :#or len(q)>=bridge_length:
            q.append(0)
            continue

        q.append(truck_weights[i])
        nowW+=truck_weights[i]
        i+=1
        
    return answer