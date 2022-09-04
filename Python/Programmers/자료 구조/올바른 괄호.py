def solution(s):
    stack=[]
    for i in s:
        if len(stack)!=0 and stack[-1]=='(' and i==')':
            stack.pop()
        else:
            stack.append(i)

    return len(stack)==0