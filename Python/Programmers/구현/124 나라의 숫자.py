def solution(n):
    answer = []
    while n!=0:
        temp=n%3
        if temp==0:
            temp=4
            n-=1
        answer.append(str(temp))
        n//=3
    return ''.join(reversed(answer))