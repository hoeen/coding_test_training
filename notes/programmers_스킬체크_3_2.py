def solution(n, m, x, y, queries):
    dx = (0, 0, -1, 1)
    dy = (-1, 1, 0, 0)
    x0, y0 = x, y
    # board = [[1]*m for _ in range(n)]
    board = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for way, dist in queries:
                nx, ny = x + dx[way]*dist, y + dy[way]*dist
                if nx < 0:
                    nx = 0
                if ny < 0:
                    ny = 0
                if nx > n-1:
                    nx = n-1
                if ny > m-1:
                    ny = m-1
                board[nx][ny] += 1
                
    answer = board[x0][y0]
    
    for b in board:
        print(b)
    
    
    
    return answer

solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]])