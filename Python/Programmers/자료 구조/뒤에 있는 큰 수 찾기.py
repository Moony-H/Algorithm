def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack=[]
    for i,num in enumerate(numbers):
        while len(stack)!=0 and stack[-1][1]<num:
            index,_=stack.pop()
            answer[index]=num
        stack.append((i,num))
        
                
        
    return answer