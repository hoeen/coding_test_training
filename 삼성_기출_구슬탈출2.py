# ~10:30
# 연결 리스트 구성
# BFS - queue, DFS - stack (재귀)
# 일단, 빨간구슬이 구멍에 들어갈때까지를 구현

n, m = map(int, input().split(' '))

# map 입력받기
board = []
for i in range(n):
    board.append(list(input()))

# dfs 구현하는데 한번에 가로 세로 끝으로 가야함
# 먼저 R,B 위치파악
def find_marble(board):
    marble_loc = {'R':None, 'B':None}
    for row in range(len(board)):
        for col in range(len(row)):
            if board[row][col] == 'R':
                marble_loc['R'] = (row,col)
            if board[row][col] == 'B':
                marble_loc['B'] = (row,col)
    return marble_loc

# 이동 함수 (상,하,좌,우 - 한방향으로 못갈때까지 움직임)
def move(x,y, way=None):
    if way == 'up':
        while board[x][y] != '#':
            x -= 1
            if board[x][y] == '#'
                x += 1
                
    elif way == 'down':
        while board[x][y] != '#':
            x += 1
            if board[x][y] == '#'
                x -= 1
    elif way == 'left':
        while board[x][y] != '#':
            y -= 1
            if board[x][y] == '#'
                y += 1
    else: #right
        while board[x][y] != '#':
            y += 1
            if board[x][y] == '#'
                y -= 1

    return x,y

# 이제 이동해서 구슬을 구멍에 넣자
rx, ry = find_marble(board)['R']
bx, by = find_marble(board)['B']

while board[rx][ry] != 'O':
    move(rx, ry, 'up')
    move(rx, ry, 'down')
    move(rx, ry, 'left')
    move(rx, ry, 'right')

    
# 유형 해법을 좀 익혀야겠다. 방향을 너무 모르겠다 ㅜ

반복문 구현?
while 10번 이하:
    move() 


def move():
    while n <= 10:
        move(up)
        
        move(down)
        
        move(left)
        
        move(right)

    return