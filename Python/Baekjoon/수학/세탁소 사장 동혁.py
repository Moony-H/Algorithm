import sys
input= sys.stdin.readline

T=int(input())
change=[25,10,5,1]
answers=[]
for i in range(T):
    answer=[]
    money=int(input())
    for j in change:
        answer.append(str(money//j))
        money=money%j
    answers.append(answer)


for i in answers:
    print(' '.join(i))

