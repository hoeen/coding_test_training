# ~11:40   ~3:30

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 0 북 1 동 2 남 3 서 
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# n, m = 3, 3
# r, c, d = 1, 1, 0
# board = [ 
# [1, 1, 1],
# [1, 0, 1],
# [1, 1, 1],
# ]

# n, m = 11, 10
# r, c, d = 7, 4, 0
# board = [ 
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
# [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
# [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
# [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
# [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
# ]


x = r
y = c

board[x][y] = 2
chore = 1

count = 0
while True:
    d -= 1
    if d < 0:
        d += 4
    nx = x + dx[d]
    ny = y + dy[d]
    
    if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 0:
            count = 0 # 초기화
            board[nx][ny] = 2 # 청소  (방문)
            chore += 1
            x, y = nx, ny # 전진
            
        elif count < 3: # 청소 이미 했거나 벽인 경우
            count += 1
            
        else: # 모든 방향 청소 돼있음
            rd = (d + 2) % 4 # 반대방향
            rx = x + dx[rd]
            ry = y + dy[rd]        
            if 0 <= rx < n and 0 <= ry < m and board[rx][ry] != 1 :
                x, y = rx, ry
                count = 0       
            else:
                break # 청소 끝     
print(chore)
        


