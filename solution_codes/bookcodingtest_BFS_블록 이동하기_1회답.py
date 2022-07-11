dx = (-1, 1, 0, 0) #상하좌우
dy = (0, 0, -1, 1)
min_time = int(1e9) 

def solution(board):
    def move(x1,y1,x2,y2,visited1,visited2,time):
        global min_time
        

        # 방문처리
        visited1[x1][y1] = True
        visited2[x2][y2] = True

        # n-1, n-1 만나면 시간 리턴 - 최소 시간 갱신
        if (x1, y1) == (n-1, n-1) or (x2, y2) == (n-1, n-1):
            if min_time > time:
                min_time = time
            return

        
        
        # 상하좌우 이동 - 동시에
        for i in range(4):
            nx1, nx2, ny1, ny2 = x1+dx[i], x2+dx[i], y1+dy[i], y2+dy[i]
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n:
                if not visited1[nx1][ny1] and not visited2[nx2][ny2] and\
                board[nx1][ny1] + board[nx2][ny2] == 0:
                    # 조건 만족시 시간 더하고 방문처리, 이동 및 재귀 들어간다.
                    # print('move:', nx1,ny1,nx2,ny2,time+1)
                    visited1[nx1][ny1] = True
                    visited2[nx2][ny2] = True
                    move(nx1,ny1,nx2,ny2,[v[:] for v in visited1],[v[:] for v in visited2],time+1)
                    # print('moveout!')
                    visited1[nx1][ny1] = False
                    visited2[nx2][ny2] = False # 회전할 경우 때문에 미방문으로 되돌림
             
        # 회전 - 이중 하나만 이동 - 두가지
        # 가로로 놓인 경우 - 1이 이동 / 2가 이동
        if x1 == x2:
            for d in [-1,1]: # x1,y1 이동
                rx1, ry1 = x2+d, y2  # 위나 아래 1이 이동
                rx2, ry2 = x1+d, y1 # 2가 이동
                if 0 <= rx1 < n and 0 <= ry1 < n:
                    if not visited1[rx1][ry1] and\
                    board[rx1][ry1] == 0 and board[rx1][y1] == 0: # 두칸 다비었는지
                        # print('rotate to ver:', rx1, ry1, x2, y2, time+1)
                        visited1[rx1][ry1] = True
                        move(rx1, ry1, x2, y2, visited1, visited2, time+1)
                        visited1[rx1][ry1] = False
                if 0 <= rx2 < n and 0 <= ry2 < n:
                    if not visited2[rx2][ry2] and\
                    board[rx2][ry2] == 0 and board[rx2][y2] == 0: # 두칸 다비었는지
                        # print('rotate to ver:', x1, y1, rx2, ry2, time+1)
                        visited2[rx2][ry2] = True
                        move(x1, y1, rx2, ry2, visited1, visited2, time+1)
                        visited2[rx2][ry2] = False
       
        elif y1 == y2:  # 세로 -> 가로로 회전
            for d in [-1,1]: # x1,y1 이동
                rx1, ry1 = x2, y2+d  # 위나 아래 1이 이동
                rx2, ry2 = x1, y1+d # 2가 이동
                if 0 <= rx1 < n and 0 <= ry1 < n:
                    if not visited1[rx1][ry1] and\
                    board[rx1][ry1] == 0 and board[x1][ry1] == 0: # 두칸 다비었는지
                        # print('rotate to hor:', rx1, ry1, x2, y2, time+1)
                        visited1[rx1][ry1] = True
                        move(rx1, ry1, x2, y2, visited1, visited2, time+1)
                        visited1[rx1][ry1] = False
                if 0 <= rx2 < n and 0 <= ry2 < n:
                    if not visited2[rx2][ry2] and\
                    board[rx2][ry2] == 0 and board[x2][ry2] == 0: # 두칸 다비었는지
                        # print('rotate to hor:', x1, y1, rx2, ry2, time+1)
                        visited2[rx2][ry2] = True
                        move(x1, y1, rx2, ry2, visited1, visited2, time+1)
                        visited2[rx2][ry2] = False    
        else:
            print('겹치거나 하여튼 잘못됨.')
        
        return    

            
    # 두칸이므로 board 두개. 0,0 / 0,1 
    # 상하좌우 동시에 움직임
    # 회전 - 둘중 하나만 - 세로 2개. 가로 2개
    n = len(board)
    visited1 = [[False]*n for _ in range(n)]
    visited2 = [[False]*n for _ in range(n)]
    # dfs - start point - (0,0), (0,1)
    # 이동조건에 다른칸 포함하기
       
    
    move(0,0,0,1,visited1,visited2,0)
    
    answer = min_time
    return answer