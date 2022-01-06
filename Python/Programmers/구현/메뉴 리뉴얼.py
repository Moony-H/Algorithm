from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer=[]
    for courseNum in course:
        courseResult=[]
        for combo in orders:
            for i in combinations(combo,courseNum):
                temp=''.join(sorted(i))
                courseResult.append(temp)
        results=Counter(courseResult).most_common()
        index=0
        while True:
            if index==len(results):
                break
            
            if results[0][1]>=2 and results[0][1]==results[index][1]:
                answer.append(results[index][0])
                index+=1
            else:
                break
    return sorted(answer)