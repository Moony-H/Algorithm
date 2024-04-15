from collections import deque

def solution(n, m, section):
    answer=0
    que=deque()
    for i in section:
        que.append(i)
    while que:
        answer+=1
        val=que.popleft()
        index=0
        for i in que:
            if(i-val+1)>m:
                break
            index+=1
        for i in range(index):
            que.popleft()
        
    return answer
        