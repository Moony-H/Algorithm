def solution(n):
    answer=0
    cache=[True for i in range(n+1)]
    
    for i in range(2,int(n**(1/2))+1):
        if cache[i]:
            j = 2
            while i * j <= n:
                cache[i*j] = False
                j += 1
    for i in range(2,n+1):
        if cache[i]:
            answer+=1

    return answer