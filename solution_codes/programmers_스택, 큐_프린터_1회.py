# ~ 10:30
from collections import deque

def solution(pri, loc):
    answer = 0
    q_pri = deque(tuple(zip(range(len(pri)), pri)))
    # (위치정보 0~n-1, 중요도)
    
    count = 0 # 인쇄된 문서 카운트
    
    while q_pri:
        # pri에서 하나빼고, 이게 뺀 큐의 max보다 큰지 판단
        position, priority = q_pri.popleft()   # 위치정보, 중요도
        if not q_pri: # 마지막까지 다뺸경우
            return count+1
        if priority >= max(q_pri, key = lambda x: x[1])[1]:
            # 뺀다
            count += 1
            if position == loc:
                return count
        else:
            q_pri.append((position, priority))

    return count