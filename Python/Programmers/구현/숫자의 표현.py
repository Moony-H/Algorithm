def solution(n):
    answer = 0
    front=0
    back=0
    num=0
    while front<=n:
        if num<n:
            front+=1
            num+=front
            if num==n:
                answer+=1
        else:
            back+=1
            num-=back
            if num==n:
                answer+=1
    
    return answer