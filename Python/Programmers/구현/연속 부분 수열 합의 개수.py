def solution(elements):
    a=set()
    elements=elements+elements
    for i in range(1,len(elements)//2+1):
        for j in range(len(elements)//2):
            a.add(sum(elements[j:j+i]))
    return len(a)