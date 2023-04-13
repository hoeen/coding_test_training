def solution(n, times):
    
    # 몇분으로 잡을때 심사가 다 되는지? 
    # 최대시간 : 사람수 * 최대시간
    max_time = n*max(times)
    start, end = 1, max_time
    answer = int(1e15)
    while start <= end:
        mid = (start + end)//2
        # mid 시간 내 심사가 다 가능한지 확인
        total = sum([mid//t for t in times])
        if total < n: # 시간내 심사 불가
            start = mid+1
        elif total >= n: # 시간내 심사 가능
            if answer > mid:
                answer = mid
            end = mid-1
    
    return answer