from collections import deque

def isCollect(l,goal):
    for i,s in enumerate(l):
        if s!=goal[i]:
            return False
    return True
        

def solution(cards1, cards2, goal):
    answer = ''
    q=deque()
    q.append(([],0,0))
    while q:
        l,index1,index2=q.popleft()
        if not isCollect(l,goal):
            continue
        elif len(l)==len(goal):
            return 'Yes'
        if index1<len(cards1):
            l.append(cards1[index1])
            q.append((l.copy(),index1+1,index2))
            l.pop()
        if index2<len(cards2):
            l.append(cards2[index2])
            q.append((l.copy(),index1,index2+1))
    return 'No'