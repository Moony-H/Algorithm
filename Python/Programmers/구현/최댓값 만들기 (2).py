def solution(n):
    n.sort(reverse=True)
    return max(n[0]*n[1],n[-1]*n[-2])