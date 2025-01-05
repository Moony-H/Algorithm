import math

def solution(n, k):
    answer=[]
    nums=[i+1 for i in range(n)]
    while nums:
        temp=math.factorial(n-1)
        answer.append(nums.pop((k//temp)+(k%temp!=0)-1))
        k%=temp
        n-=1
    return answer