def solution(N, number):
    answer = -1
    cache=[]

    for i in range(1,9):
        cases=set()
        check=int(str(N)*i)
        cases.add(check)

        for j in range(0,i-1):
            for temp1 in cache[j]:
                for temp2 in cache[-j-1]:
                    cases.add(temp1-temp2)
                    cases.add(temp1+temp2)
                    cases.add(temp1*temp2)
                    if temp2!=0:
                        cases.add(temp1//temp2)
        if number in cases:
            answer=i
            break
        cache.append(cases)
    return answer