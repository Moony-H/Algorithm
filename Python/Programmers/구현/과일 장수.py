def solution(k, m, score):
    answer = 0
    arr=sorted(score)[len(score)%m:]
    for i in range(len(arr)//m):
        sub=arr[i*m:(i+1)*m]
        answer+=sub[0]*m
    return answer