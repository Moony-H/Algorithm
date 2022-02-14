def solution(n, lost, reserve):
    reserve.sort()
    
    
    for i in reserve[:]:
        if i in lost:
            del lost[lost.index(i)]
            del reserve[reserve.index(i)]
    for i in reserve:
        if i-1 in lost:
            del lost[lost.index(i-1)]
        elif i+1 in lost:
            del lost[lost.index(i+1)]
            
    return n - len(lost)