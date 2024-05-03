from collections import deque

def checkStack(que,stack):
    result=0
    while len(stack)>0 and len(que)>0 and stack[-1]==que[0]:
        result+=1
        stack.pop()
        que.popleft()
    return result


def solution(order):
    answer = 0
    stack=[]
    que=deque(order)
    
    for i in range(1,len(order)+1):
        answer+=checkStack(que,stack)
        if que[0] == i:
            answer+=1
            que.popleft()
        else:
            stack.append(i)
        
    answer+=checkStack(que,stack)
                
    return answer