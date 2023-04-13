def solution(numbers, target):
    global count
    count = 0
    # 플러스 마이너스 번갈아 트리 탐색
    def dfs(seq, cal):
        global count
        if not seq: # 빈 리스트
            if cal == target:
                count += 1
            return
        new_cal = cal + seq[0]
        dfs(seq[1:], new_cal)
        new_cal = cal - seq[0]
        dfs(seq[1:], new_cal)
    
    
    dfs(numbers, 0)
    
    
    return count