def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]
    board[0][0] = 1 # 시작점 1
    for px, py in puddles:
        board[py-1][px-1] = -1
    for x in range(n):
        for y in range(m):
            # print(x,y)
            if board[x][y] == -1: # 물이면:
                continue # 다음칸으로
            # print('not water')
            now = 0
            lx, ly = x, y-1 # 왼쪽칸
            ux, uy = x-1, y # 윗칸
            if 0 <= lx and 0 <= ly:
                if board[lx][ly] >= 0: # 물 아니면
                    now += board[lx][ly]
            if 0 <= ux and 0 <= uy:
                if board[ux][uy] >= 0:
                    now += board[ux][uy]
            board[x][y] += now
            
    #         print('board;')
    #         for b in board:
    #             print(b)
    # print('result:', board[n-1][m-1] % 1000000007)
                
    return board[n-1][m-1] % 1000000007