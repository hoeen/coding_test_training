n,m,x,y,k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

order = list(map(int, input().split()))

opp = {
    1:6,
    2:5,
    3:4,
    4:3,
    5:2,
    6:1
}

# 이동 -> 복사 (주사위 dict에 반영) -> 상단 출력
# 처음 놓인 top 과 down
top = 1
front = 5
right = 3

# 이동
def move(ord):  # 주사위 상태를 바꿈.
    global top, front, right
    if ord == 1: # 동
        track = [top,right,opp[top],opp[right]] # 트랙 설정
        right = top
        top = track[(track.index(top)-1)]
        # front 그대로
    elif ord == 2: # 서
        track = [top,right,opp[top],opp[right]] # 트랙 설정
        right = opp[top]
        top = track[(track.index(top)+1) % 4]
    elif ord == 3: # 북
        track = [top, front, opp[top], opp[front]]
        front = opp[top]
        top = track[(track.index(top)+1) % 4]
        # print('dice: ',top,front,right)
    else: # 4 남
        track = [top, front, opp[top], opp[front]]
        front = top
        top = track[(track.index(top)-1)]
    
# 실제 이동 하면서 번호 바꾸기
written = { 
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for ord in order: #1,2,3,4
    if x+dx[ord-1] < 0 or y+dy[ord-1] < 0 or x+dx[ord-1] >= n or y+dy[ord-1] >= m:
        continue
    move(ord)
    x += dx[ord-1]
    y += dy[ord-1]
    if board[x][y] == 0:
        board[x][y] = written[opp[top]] # 바닥면 숫자를 칸에 복사
    else:
        written[opp[top]] = board[x][y] # 주사위에 칸숫자 복사
        board[x][y] = 0 
   
    print(written[top])
    
    
   
    


