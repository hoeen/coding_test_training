# 11:00
# from collections import deque

def solution(n, computers):
    answer = 0 # 네트워크 개수
    '''
    0 ~ n-1 을 visited
    돌면서 각 행에 연결정보 있는지 체크. 큐에 넣는다 (자기자신 빼고)
    '''
    visited = [False]*(n)
    
    for i in range(n):
        queue = []
        if not visited[i]:
            queue.append(i)
            while queue:
                q = queue.pop(0)
                for y in range(n):
                    if q != y and computers[q][y] == 1 and not visited[y]:
                        queue.append(y)
                        visited[y] = True
            answer += 1
    
    return answer