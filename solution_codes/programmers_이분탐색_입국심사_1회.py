# ~ 3:30 50분  - 4:40 분에 품. 총 110분 소요.
ans_cand = int(1e9)**2

def solution(n, times):
    def binary_search(array, start, end):
        global ans_cand
        if start > end:
            return False
        else:
            mid = (start + end) // 2
            cand_time = array[mid]
            nc = 0
            for t in times:
                nc += cand_time//t   
            if nc < n: #  더 적은 사람밖에 안됨 - 큰쪽 탐색
                return binary_search(array, mid+1, end)
            else: # 맞아떨어짐 - 더 작은쪽 있는지 탐색
                if ans_cand > cand_time:
                    ans_cand = cand_time
                return binary_search(array, start, mid-1)
    
    grid = range(n*min(times)+1)
    
    binary_search(grid, 0, len(grid)-1)
    
    
    return ans_cand



