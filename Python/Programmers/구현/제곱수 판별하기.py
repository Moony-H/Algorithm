import math
def solution(n):
    return 1<<(len(str(math.sqrt(n)).split(".")[1])>1)