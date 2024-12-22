def solution(n):
    cache=[1]*n
    cache[0]=1
    if n==1: return 1
    if n==2: return 2
    cache[1]=2
    for i in range(2,n):
        cache[i]=(cache[i-1]+cache[i-2])%1000000007
    return cache[-1]