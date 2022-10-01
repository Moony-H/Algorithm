cache=[-1]*100001

def f(n):
    if cache[n]!=-1:
        return cache[n]
    cache[n]=f(n-1)+f(n-2)
    return cache[n]

def solution(n):
    answer = 0
    cache[0]=0
    cache[1]=1
    cache[2]=1
    return f(n)

print(solution(100))
