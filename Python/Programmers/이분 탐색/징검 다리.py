def solution(distance, rocks, n):
    answer = 0
    l, r = 0, distance
    
    rocks.sort()
    
    while l <= r: 
        mid = (l + r) // 2 
        removed = 0 
        std = 0 
        for rock in rocks:
            if rock - std <  mid:
                removed += 1 
            else:
                std = rock
                
            if removed > n:
            	break
                
        if removed > n:
            r = mid - 1
        else:
            answer = mid
            l = mid + 1
            
    return answer