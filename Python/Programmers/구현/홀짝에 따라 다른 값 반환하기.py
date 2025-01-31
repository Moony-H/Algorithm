def solution(n):
    return int(''.join([str(i) for i in n if i%2==0])) + int(''.join([str(i) for i in n if i%2!=0]))