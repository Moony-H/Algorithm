import itertools




a=['ABBAC','ACDDE','CEADB','CEEED']
wanted=[2,3,4]

orders=[]
for i in a:
    orders.append("".join(sorted(i)))#문자열을 기준으로 합치기


print(orders)

b=[]
for i in a:
    b.append(list(set(sorted(i))))


c=[i for k in b for i in k]

c=list(set(sorted(c)))

c.sort()
d=[]
for i in wanted:
    d.append(sorted(list(sorted(itertools.combinations(c,i)))))#itertools의 조합(c)으로 i개 선택하여 반환한 걸 솔트, 그리고 list화 시켜서 다시 sort.

e=[''.join(i) for j in d for i in j]



print(e)

result=[0 for _ in e]

print(result)
for j in orders:
    print(j)
    for i in range(len(e)):
        print(e[i])
        if e[i] in j:
            result[i]+=1
print(result)