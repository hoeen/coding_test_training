from collections import deque

n, m = map(int, input().split())

ocean = []
for _ in range(n):
    ocean.append(list(map(int, input().split())))

dx = (-1,1,0,0) # 상하좌우
dy = (0,0,-1,1)

def melt():
    global ocean
    melted = [o[:] for o in ocean]
    for x in range(n):
        for y in range(m):
            if ocean[x][y] > 0: # 빙산일때
                for i in range(4):
                    nx = x + dx[i] # 주위 바다 조사
                    ny = y + dy[i]
                    if ocean[nx][ny] == 0 and melted[x][y] != 0:
                        melted[x][y] -= 1
    ocean = [m[:] for m in melted]

def pick():
    for x in range(n):
        for y in range(m):
            if ocean[x][y] > 0:
                return x, y
                
# bfs
def bfs():
    # 빙산 하나 찾기
    x, y = pick()

    # print('find', x, y)
    q = deque()
    visited = [[False]*m for _ in range(n)]
    q.append((x,y))
    visited[x][y] = True
    while q:
        fx, fy = q.popleft()
        for i in range(4):
            nx = fx + dx[i]
            ny = fy + dy[i]
            if (0 <= nx < n and 0 <= ny < m) and ocean[nx][ny] > 0 and \
                not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
        

    return visited

def find_div(visited):
    # visited False 중 0이 아닌 게 있으면 나눠진거임.
    for x in range(n):
        for y in range(m):
            if ocean[x][y] > 0 and not visited[x][y]:
                return True
    return False

time = 0
while True:
    time += 1
    melt()
    if sum([sum(o) for o in ocean]) == 0:
        print(0)
        break
    else:
        visited = bfs()

    if find_div(visited):
        print(time)
        break
    
    