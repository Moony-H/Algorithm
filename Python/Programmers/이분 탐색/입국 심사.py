def solution(n, times):
    answer = 0
    left = 0
    right = max(times)*n
    while left < right:
        mid = (left+right)//2
        peopleInTime = 0
        for i in times:
            peopleInTime += mid//i
        if peopleInTime >= n:
            right = mid
        else:
            left = mid+1

    return left
