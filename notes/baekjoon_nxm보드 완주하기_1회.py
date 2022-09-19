# ~ 9:15
case = 0
size = input()
while size:
    n, m = map(int, size.split())
    case += 1




# n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]

# n, m = 5, 5
# board = [
# list('**...'),
# list('.....'),
# list('....*'),
# list('..*..'),
# list('.....')
# ]

# n, m = 3, 4
# board = [
#     list('****'),
#     list('*...'),
#     list('*..*')
# ]

# for b in board:
#     print(b)

    dx = (-1, 0, 1, 0) # 상 우 하 좌 - 시계방향
    dy = (0, 1, 0, -1)

    visited = [[0]*m for _ in range(n)]


    min_step = int(1e9)
    def dfs(x, y, visited, step, d):
        global min_step
        def go():
            rx, ry = x, y
            cango = True
            while cango:
                visited[rx][ry] = step
                nx, ny = rx + dx[d], ry + dy[d]
                cango = False
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == 0 and board[nx][ny] != '*':
                        cango = True
                        rx, ry = nx, ny
            # print('go - visited:')
            # for v in visited:
            #     print(v)
            return rx, ry

        def ungo(ux, uy):
            cango = True
            ud = (d+2) % 4
            while cango:
                visited[ux][uy] = 0
                nx, ny = ux + dx[ud], uy + dy[ud] #반대 방향
                cango = False
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == step and board[nx][ny] != '*':
                        cango = True
                        ux, uy = nx, ny
            # print('ungo - visited:')
            # for v in visited:
            #     print(v)
            return



        gx, gy = go() # gx, gy 도 visited 됨
        # 다음 방향 탐색
        for j in range(4):
            nx, ny = gx + dx[j], gy + dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] != '*': # 갈수있는 방향이면
                    dfs(nx, ny, [v for v in visited], step+1, j)

        # 다 탐색해서 갈곳 없으면 visited 체크 후 모두 방문했을시 단계 업데이트
        for r in range(n):
            for c in range(m):
                if visited[r][c] == 0 and board[r][c] == '.': # 방문 안했는데 빈칸이다
                    ungo(gx, gy)
                    return

        ungo(gx, gy)
        if min_step > step:
            min_step = step
            return

    for x in range(n):
        for y in range(m):
            for i in range(4):
                dfs(x, y, [v for v in visited], 1, i) #step 1부터

    if min_step == int(1e9):
        answer = -1
    else:
        answer = min_step

    print(f'Case {case}: {answer}')



    size = input()