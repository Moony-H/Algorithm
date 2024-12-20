def solution(n,a,b):
    answer = 1
    mn=min(a,b)
    mx=max(a,b)
    while mx-mn!=1 or mn%2==0:
        mn=mn//2+mn%2
        mx=mx//2+mx%2
        answer+=1

    return answer