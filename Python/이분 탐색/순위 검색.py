from itertools import combinations
from bisect import bisect_left
def pick(string):
    oneInfo=list(string.split())
    point=int(oneInfo[-1])
    result=[]
    for i in range(5):
        
        choice=list(combinations((0,1,2,3),i))
        for j in choice:
            temp=['-','-','-','-']
            for k in j:
                temp[k]=oneInfo[k]
            result.append([' and '.join(temp),point])
    return result