def solution(s):
    answer = []
    arr=s[2:-2].split('},{')
    s=[]
    for i in arr:
        s.append(list(map(int,i.split(','))))
    s.sort(key=len)
    for i in s:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer