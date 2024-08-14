import heapq

def solution(k, score):
    hq=[]
    answer=[]
    for i in score:
        heapq.heappush(hq,i)
        if(len(hq)>k):
            heapq.heappop(hq)
        answer.append(hq[0])
    return answer