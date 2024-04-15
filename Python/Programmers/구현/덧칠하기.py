def solution(n, m, section):
    return (section[-1]-section[0]+1)//m + (1 if (section[-1]-section[0]+1)%m!=0 else 0)