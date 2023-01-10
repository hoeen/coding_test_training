# 우석 - 두 큐 합 같게 만들기
from collections import deque
import copy

def solution(queue1, queue2):
    
    queue1, queue2 = deque(queue1), deque(queue2)


    # 합을 같게 만들 수 있으므로, greedy로 크면 빼고 작으면 넣는 식으로 간다.
    # 상태들을 저장하고 혹시 같은 상태가 오면 -1
    answer = 0
    s1, s2 = sum(queue1), sum(queue2)
    init1 = copy.deepcopy(queue1)
    init2 = copy.deepcopy(queue2)
    
    while True:
        if answer > int(1e6):
            return -1
        
        if s1 > s2:
            qpop = queue1.popleft()
            queue2.append(qpop)
            s1 -= qpop
            s2 += qpop
            if queue1 == init1 or queue1 == init2 :
                return -1
            
            answer += 1
            
        elif s1 < s2:
            qpop = queue2.popleft()
            queue1.append(qpop)
            s1 += qpop
            s2 -= qpop
            if queue1 == init1 or queue1 == init2:
                
                return -1
            answer += 1
        else:
            return answer
       