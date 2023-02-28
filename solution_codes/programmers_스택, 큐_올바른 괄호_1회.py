from collections import deque

def solution(s):
    answer = True
    oc = 0 
    qs = deque(s)
    while qs:
        q = qs.popleft()
        if q == '(':
            oc += 1
        else:
            oc -= 1
        if oc < 0:
            return False
        
        
    if oc != 0:
        return False

    return answer