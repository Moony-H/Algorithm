def solution(data, col, row_begin, row_end):
    answer = 0
    data=sorted(data, key=lambda x:(x[col-1],-x[0]))
    results=[]
    for i in range(row_begin-1,row_end):
        modResult=0
        for j in data[i]:
            modResult+=j%(i+1)
        results.append(modResult)
    answer=results[0]
    for i in results[1:]:
        answer=answer ^ i
    return answer