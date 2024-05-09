def solution(want, number, discount):
    answer = 0
    for i in range(0,len(discount)-9):
        c=discount[i:i+10]
        for j in range(len(want)):
            if c.count(want[j])!=number[j]:
                break
        else:
            answer+=1
                        
    return answer