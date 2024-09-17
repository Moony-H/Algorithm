
def same(stack):
    return stack==[1,2,3,1]
        

def solution(ingredient):
    answer = 0
    stack=[]
    for i in ingredient:
        stack.append(i)
        if(len(stack)<4):
            continue
        while(same(stack[len(stack)-4:len(stack)])):
            for _ in range(4):
                stack.pop(-1)
            answer+=1
            
    return answer