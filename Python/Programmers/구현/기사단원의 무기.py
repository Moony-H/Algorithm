import math

def getAns(n,l,p):
    count=0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if i ** 2 != n:
                count += 1
        if count>l:
            return p
    return count

def solution(n, l, p):
    answer = 0
    return sum([getAns(i+1,l,p) for i in range(n)])
