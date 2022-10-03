def solution(arr):
    answer = 0
    m=max(arr)
    a=0
    done=False
    while not done:
        a+=m
        done=True
        for i in arr:
            if a%i!=0:
                done=False
        
                
    return a