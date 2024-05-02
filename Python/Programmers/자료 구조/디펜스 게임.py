import heapq

def solution(n, k, enemy):
    answer = 0
    q=[]
    for i in enemy:
        heapq.heappush(q,-i)
        if n-i<0 and k>0:
            k-=1
            point= heapq.heappop(q) if len(q)>0 else 0
            n-=point
        n-=i
        if n<0:
            return answer
        answer+=1
    return answer