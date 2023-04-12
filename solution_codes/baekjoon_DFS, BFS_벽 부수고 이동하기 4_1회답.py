from collections import deque, defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]


dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

visited = [[False]*m for _ in range(n)]
total_visited = [[0]*m for _ in range(n)] # 참조할 칸. [그룹숫자]
group_ref = defaultdict(int)


def bfs(x, y, gnum):
    # global total_visited
    # global group_ref
    
    '''
    뚫려있는 칸 개수만큼 찾은 방향의 visited 칸을 모두 업데이트
    '''
    count = 1 # 이동할수있는 빈칸
    # found = deque([]) # 찾은칸
    q = deque([])
    q.append((x, y))
    visited[x][y] = True
    total_visited[x][y] = gnum
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and not visited[nx][ny] and total_visited[nx][ny] == 0:
                    visited[nx][ny] = True
                    total_visited[nx][ny] = gnum
                    count += 1
                    q.append((nx, ny))
                    
    # 기억할 부분 넣어야함 - 찾은 빈칸개수로 채우기
    group_ref[gnum] = count
    return

current = 1 # 현재 체크할 그룹 넘버
for x in range(n):
    for y in range(m):
        # 빈칸을 탐색
        if board[x][y] == 0 and not visited[x][y]:
            bfs(x, y, current)
            current += 1
            

for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            gset = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    gset.add(total_visited[nx][ny])
            board[x][y] = (board[x][y] + sum(group_ref[num] for num in gset)) % 10
    

for b in board:
    print(''.join(list(map(str,b))))