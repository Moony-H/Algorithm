def solution(prices):
    answer=[0 for _ in prices]
    stack=[]
    for i,n in enumerate(prices):
        while stack and stack[-1][1]>n:
            temp=stack.pop()
            answer[temp[0]]=i-temp[0]
        stack.append((i,n))
    for i in stack:
        answer[i[0]]=len(prices)-i[0]-1
            
    return answer