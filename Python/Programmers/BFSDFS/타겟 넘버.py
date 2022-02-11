from collections import deque

def solution(numbers, target):
    answer = 0
    length=len(numbers)
    que=deque()
    que.append((0,0))
    while que:
        val,num=que.popleft()
        if val==target and num==length:
            answer+=1
        if num!=length:
            que.append((val+numbers[num],num+1))
            que.append((val-numbers[num],num+1))
    return answer