import itertools

array=[0 for _ in range(1000001)]

a=int(input())
array[1]=0
array[2]=1



for i in range(3,a+1):
    temp=[1000001,1000001,1000001]
    if i%2==0:
        temp[0]=array[int(i/2)]+1
    if i%3==0:
        temp[1]=array[int(i/3)]+1
    temp[2]=array[i-1]+1
    result=temp[0]
    for j in range(len(temp)):
        if temp[j]!=0 and temp[j]<result:
            result=temp[j]
    array[i]=result


print(array[a])
