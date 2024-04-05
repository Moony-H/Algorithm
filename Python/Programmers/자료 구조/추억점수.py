def solution(name, yearning, photo):
    answer = []
    points={}

    for i in range(len(name)):
        points[name[i]]=yearning[i]

    for i in photo:
        result=0
        for j in i:
            if j not in points:
                continue
            result+=points[j]
        answer.append(result)

    return answer