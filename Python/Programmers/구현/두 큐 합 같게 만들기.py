from collections import deque

def solution(queue1, queue2):
    answer = 0

    q1=deque(queue1)
    q2=deque(queue2)
    
    q1Sum=sum(q1)
    q2Sum=sum(q2)

    for i in  range(len(q1)*3):
        if(q1Sum>q2Sum):
            temp=q1.popleft()
            q2.append(temp)
            q1Sum-=temp
            q2Sum+=temp
            
        elif q2Sum>q1Sum:
            temp=q2.popleft()
            q1.append(temp)
            q1Sum+=temp
            q2Sum-=temp
            
        else:
            return i
    return -1