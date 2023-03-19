# ~11:15 10분
from collections import deque

def solution(prices):
    time = 0
    answer = []
    q = deque(prices)
    while q:
        notdec = 0
        cur = q.popleft()
        for fp in q:
            if fp >= cur:
                notdec += 1
        answer.append(notdec)
        
    
    return answer