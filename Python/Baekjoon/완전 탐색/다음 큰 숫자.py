def solution(n):
    answer = 0
    num=bin(n).count('1')
    for i in range(n+1,1000001):
        n=bin(i).count('1')
        if n==num:
            return i
    return answer