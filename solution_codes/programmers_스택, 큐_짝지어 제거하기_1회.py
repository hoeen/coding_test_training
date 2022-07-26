from collections import deque

def solution(s):
    q = deque([])
    if len(s) == 1:
        return 0
    po = 0
    while po < len(s):
        if po == len(s) - 1:
            q.append(s[po])
            po += 1
        elif s[po+1] != s[po]:
            q.append(s[po])
            po += 1
        else: # 다음것이 같은 문자면
            po += 2 # 다음 다음으로 이동
            if po > len(s)-1:
                break
            while q:
                qnum = q.pop()
                if qnum == s[po]: #그다음것이 q있는것이랑 같다면
                    po += 1 # 그다음으로 이동
                else:
                    q.append(qnum) # 다시 q에 넣음
                    break # q랑 다음것이 다르면, 빠져나옴
                    
    return 0 if q else 1  # q가 남아 있으면 제거 못했으므로 0, q가 비었다면 다 제거한 것이므로 1