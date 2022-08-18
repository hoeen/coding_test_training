# BFS로 접근
from collections import deque

f,s,g,u,d = map(int, input().split())

# 각 층에 방문했을때 visit 처리
q = deque([])
visited = [None]*(f+1)
# 시작층 큐에 삽입
q.append((s,0)) # (층, 버튼횟수)
while q:
    now, pressed = q.popleft()
    # print(now, pressed)
    # print(visited)
    
    if visited[now] is None:
        visited[now] = pressed # 꺼낸 층에 방문처리
        # 층 도달하면 반환
        if now == g:
            break
        up = now + u
        down = now - d
        if 0 < up <= f:
            q.append((up, pressed+1))
        if 0 < down <= f:
            q.append((down, pressed+1))
    # print('q status:', q)
    
# print('visit changed:', visited)
if visited[g] is not None:
    print(visited[g])
else:
    print('use the stairs')
