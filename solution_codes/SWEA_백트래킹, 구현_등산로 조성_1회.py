# ~ 5:40
# ~ 6:00

n, k = 5, 1       
board = [
[9, 3, 2, 3, 2], 
[6, 3, 1, 7, 5],
[3, 4, 8, 9, 9],
[2, 3, 7, 7, 7],
[7, 6, 5, 5, 8]
]

n, k = 3, 2       
board = [
[1, 2, 1],     
[2, 1, 2],
[1, 2, 1]
]

def find_peaks():
    peak = 1
    peak_list = []
    for row in board:
        if max(row) > peak:
            peak = max(row)
    for x in range(n):
        for y in range(n):
            if board[x][y] == peak:
                peak_list.append((x,y))
    return peak_list

# [상 하 좌 우]로 주위 차이 구하는 함수
def diff(x, y, visited):
    diff_list = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # print('nx,ny:', nx, ny)
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                diff_list.append(board[nx][ny] - board[x][y])
            else:
                diff_list.append(-100)
        else:
            diff_list.append(-100)
    return diff_list


def makeroad(x, y, visited, length, const=False):
    global max_length

    
    

    # 방문처리, 등산로 길이 갱신
    visited[x][y] = True
    length += 1

    # 중간과정 체크
    # print(x, y, length, const)
    
    
    
    

    # 공사 안했으면 - 깎고 진행, 그대로 안하고 넘길수도 있음.
    if not const:
        # print('not const')
        # 차이 구하기
        diff_list = diff(x, y, visited)
        # print('diffxy:', x, y, visited)
        # print('diff:', diff_list)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if diff_list[i] >= 0 and diff_list[i] < k: 
                for cut in range(diff_list[i]+1, min(board[nx][ny], k)+1):
                    # print('cutted', cut)
                    board[nx][ny] -= cut
                    
                    # 주위 살펴서 낮은 곳 찾기
                    for i in range(4):
                        mx = x + dx[i]
                        my = y + dy[i]

                        # 낮은 곳 찾으면 length 1 더하고 재귀
                        if 0 <= mx < n and 0 <= my < n:
                            if board[mx][my] < board[x][y] and\
                                not visited[mx][my]:
                                makeroad(mx, my, [v[:] for v in visited], length, True)
                    board[nx][ny] += cut
        # 안깎고 그냥 진행
        # 낮은 곳 찾으면 length 1 더하고 재귀
        # 주위 살펴서 낮은 곳 찾기
        # print('not const but go')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] < board[x][y] and\
                    not visited[nx][ny]:
                    makeroad(nx, ny, [v[:] for v in visited], length, const)
    
    # 이전에 공사 진행한경우: 안깎고 진행
    else: 
        # print('already const')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] < board[x][y] and\
                    not visited[nx][ny]:
                    makeroad(nx, ny, [v[:] for v in visited], length, const)
        

    # 주위에 더 낮은 곳 없으면 최대 길이 갱신후 종료
    if max_length < length:
        max_length = length
    
    # 어떻게 깎지? 주위에 하나 골라서 1~k까지 깎아놓고 진행한다.
    # 그럼 깎을필요 없는경우는? - 깎아봤자 길 없는경우. 즉 주위가 모두 k보다 높은경우
    # k보다 차이가 작은경우, 1~k-1만큼 깎아본다. 

    return 

    


peaks = find_peaks()
max_length = 0
dx = (-1, 1, 0, 0) # 상하좌우
dy = (0, 0, -1, 1)


for x, y in peaks:
    # print('peak start:', x, y)
    visited = [[False]*n for _ in range(n)]
    makeroad(x, y, visited, 0)

print(max_length)