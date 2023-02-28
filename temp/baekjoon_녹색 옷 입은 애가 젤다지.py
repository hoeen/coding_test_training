n = int(input())
# 최소 금액 잃으며 끝까지 이동

board = [list(map(int, input().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

min_lup = int(1e9)

def dfs(x, y, visited, lup):
    
    global min_lup

    new_visited = [v[:] for v in visited]
    new_visited[x][y] = True
    # n-1, n-1 에서 최소금액 갱신 후 종료
    if (x, y) == (n-1, n-1):
        if min_lup > lup:
            min_lup = lup
        return

    # x, y 네방향으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not new_visited[nx][ny]:
                new_lup = lup + board[nx][ny]
                dfs(nx, ny, new_visited, new_lup)
    
    return

visited = [[False]*n for _ in range(n)]
# visited[0][0] = True
dfs(0, 0, visited, board[0][0])
print(min_lup)
        
        


    

