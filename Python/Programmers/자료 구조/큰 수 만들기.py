def solution(number, k):
    stack=[]
    for i in map(int,number):
        while k>0 and len(stack)!=0 and stack[-1]<i:
            k-=1
            stack.pop()
        stack.append(i)
    return ''.join(map(str,stack[:len(stack)-k]))