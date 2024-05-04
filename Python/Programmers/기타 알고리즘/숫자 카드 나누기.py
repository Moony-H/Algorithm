def gcd(m,n):
    if n>m:
        m,n=n,m
    if m%n==0:
        return n
    return gcd(m%n,n)

def getListGcd(l):
    result=l[0]
    for i in l[1:]:
        result=gcd(i,result)
    return result

def getGcdResult(l,gcd):
    for i in l:
        if i%gcd==0:
            return 0
    return gcd

def solution(arrayA, arrayB):
    answer = 0
    # gcd는 두개의 최대공약수를 구하는 함수이다. 여러개의 최대공약수를 구하자.
    gcdA=getListGcd(arrayA)
    gcdB=getListGcd(arrayB)
    
    answer=getGcdResult(arrayA,gcdB)
    answer=max(answer,getGcdResult(arrayB,gcdA))
        
    
    return answer