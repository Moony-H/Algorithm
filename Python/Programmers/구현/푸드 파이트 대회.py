def solution(food):
    temp=[str(i)*(food[i]//2) for i in range(1,len(food))]
    return ''.join(temp)+'0'+''.join(reversed(temp))