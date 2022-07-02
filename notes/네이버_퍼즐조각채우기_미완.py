from collections import deque
from copy import deepcopy as dcopy

# game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
# table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]


def solution(game_board, table):
    global answer
    answer = 0
    
    # 상하좌우
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)
    
    def bfs(x, y):
        n = len(game_board)
        visited = [[False]*n for _ in range(n)]
        q = deque([]) #bfs - filo

        q.append((x,y))
        visited[x][y] = True

        while q:
            qx, qy = q.popleft()
            for i in range(4):
                nx, ny = qx+dx[i], qy+dy[i]
                if (0 <= nx < n) and (0 <= ny < n):
                    if table[nx][ny] == 1 and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True

        new_board = [[0]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if visited[x][y]:
                    new_board[x][y] = 1
                    table[x][y] = 0 # 조각 테이블에서 조각을 없앰
        
        return new_board
    
    # 회전 함수
    def rotation_clock(piece):
        rot_piece = [[0]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if piece[x][y] == 1:
                    rot_piece[y][n-1-x] = 1
        return rot_piece
    
    # 게임보드 1의 수를 저장해둠
    def board_count(board):
        res = 0
        for row in board:
            res += row.count(1)
        return res
    
    
    def fill(piece, big_board): #piece = pieces[k]
        global answer
        filled = False
        # print(piece)
        # center_board = big_board[n:2*n][n:2*n]
        for i in range(4): # all_pieces[i] 4개
            for bx in range(1, 2*n-1):
                for by in range(1, 2*n-1):
                    # 슬라이딩으로 이동하며 수를 더함. 중심부분의 1개수가 원래 블록수만큼 더해지면 채워들어간거.
                    for ix in range(n):
                        for iy in range(n):
                            big_board[ix+bx][iy+by] += piece[i][ix][iy]
                    if board_count(game_board) == board_count(big_board) - board_count(piece[i]):
                        print('matched. empty check', (bx, by))
                        # 주변에 빈칸 없는지 검사
                        empty = False
                        for ix in range(n):
                            for iy in range(n):
                                if piece[i][ix][iy] == 1:
                                    for d in range(4):
                                        nx, ny = ix+dx[d], iy+dy[d]
                                        if big_board[nx+bx][ny+by] == 0:
                                            empty = True
                        if not empty:
                            print('fill! ', answer, board_count(piece[i]))
                            for p in piece[i]:
                                print(p)
                            answer += board_count(piece[i])
                            filled = True
                            # 갱신된 big board
                            center_board = [b[n:2*n] for b in big_board[n:2*n]]
                            big_board = [[-2]*n*3 for _ in range(n*3)]
                            for x in range(n):
                                for y in range(n):
                                    big_board[x+n][y+n] = center_board[x][y]
                                
                            return big_board
                        else:
                        # 다시 원복
                            for ix in range(n):
                                for iy in range(n):
                                    big_board[ix+bx][iy+by] -= piece[i][ix][iy]
                    
                    else:
                    # 다시 원복
                        for ix in range(n):
                            for iy in range(n):
                                big_board[ix+bx][iy+by] -= piece[i][ix][iy]
                            # a = 1
        return big_board            
    
    # 퍼즐 개수만큼의 table 생성
    n = len(game_board)
    pieces = []
    for x in range(n):
        for y in range(n):
            if table[x][y] == 1:
                pieces.append(bfs(x,y))
    
    all_pieces = {}
    for k in range(len(pieces)):
        rot_pieces = [pieces[k]]
        for _ in range(3):
            rotp = rotation_clock(rot_pieces[-1])
            rot_pieces.append(rotp)
        all_pieces[k] = rot_pieces
    
    big_board = [[-2]*n*3 for _ in range(n*3)]
    for x in range(n):
        for y in range(n):
            big_board[x+n][y+n] = game_board[x][y]
    
    
    
    
    
    
    for k in range(len(pieces)):
        print(f'{k}th piece')
        big_board_new = fill(all_pieces[k], big_board)
        big_board = dcopy(big_board_new)
        
    print('result')
    for b in big_board:
        print(b)
    return answer



