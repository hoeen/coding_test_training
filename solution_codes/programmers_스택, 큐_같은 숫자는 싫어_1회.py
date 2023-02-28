from collections import deque

def solution(arr):
    q = deque(arr)
    p1 = q.popleft()
    ans = deque([])
    if not q:
        return arr
    while q:
        
        p2 = q.popleft() # 하나 더뽑음

        if p1 == p2:
            if not q:
                ans.append(p1)
            continue
        else:
            ans.append(p1)
            p1 = p2
            if not q:
                ans.append(p2)
            
    return list(ans)
