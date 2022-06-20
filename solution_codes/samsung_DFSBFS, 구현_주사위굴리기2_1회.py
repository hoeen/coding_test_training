'''
(1,1). 처음 동쪽으로 이동
이동방향에 칸이 없다면, 반대로 해서 한칸
칸에 대한 점수 획득
칸점수, 주사위 바닥점수 비교하여 이동 결정
주사위 큰경우 시계 방향 회전
작은경우 반시계
같은경우 이동 방향 변화 없음

칸 점수 구하는방법 - 
있는칸에서 동서남북 연속해서 이동하는 칸의 수를 모두 구함(첫칸이랑 같은숫자일때)
점수 = 첫칸 * 이동칸수

각 이동에서 획득하는 점수합을 구해보자!
'''
n, m, k = map(int, input().split()) # k는 이동횟수

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))



# 주사위 이동하면서 업데이트
# 동서 - front 그대로, 남북 - right 그대로.
# bottom 항상 업데이트. 두 면만 정해지면 나머지는 알아서 정해짐.
opp = {
    1:6,
    2:5,
    3:4,
    4:3,
    5:2,
    6:1
}
front = 5
right = 3
bottom = 6

now_di = 1
x, y = 0, 0

opp_di = {
    0:2,
    2:0,
    1:3,
    3:1
}

# 상하좌우  북동남서 0312 북남서동 0123
dx = (-1,0,1,0) #(-1,1,0,0)
dy = (0,1,0,-1) #(0,0,-1,1)

# 방향 정해지면 어떻게 f,r,b가 바뀌지? 상, 하, 좌, 우
def dice(di):
    global front, right, bottom
    if di == 0: # 북
        nbottom = opp[front]
        nright = right
        nfront = bottom
    elif di == 1: # 동
        nbottom = right
        nright = opp[bottom]
        nfront = front
    elif di == 2: # 남
        nbottom = front
        nright = right
        nfront = opp[bottom]
    else: # 서
        nbottom = opp[right]
        nright = bottom
        nfront = front
    
        
    
    # 현재 상태 변환
    front, right, bottom = nfront, nright, nbottom
    # print('f:', front, 'r:', right, 'b:', bottom)

total_score = 0
for i in range(k): # k 번 이동
    ix, iy = x+dx[now_di], y+dy[now_di]
    
    if (0 <= ix < n and 0 <= iy < m):
        dice(now_di)
        ox, oy = x+dx[now_di], y+dy[now_di]
    
    else:
        # 범위 벗어나면 반대방향으로 한칸 전진
        now_di = opp_di[now_di]
        dice(now_di)
        ox, oy = x+dx[now_di], y+dy[now_di]
    # print('now di:', now_di)
    # print('now:', ox,oy)
    # 칸점수
    now_board = board[ox][oy]
    
    # bfs 로 가능한 칸수 구함
    pos_score = 1
    visited = [[False]*m for _ in range(n)]
    visited[ox][oy] = True # 첫 방문처리
    q = [(ox,oy)]
    while q:
        bx, by = q.pop(0)
        for i in range(4):
            tx, ty = bx + dx[i], by + dy[i]
            if (0 <= tx < n and 0 <= ty < m) and \
                board[tx][ty] == now_board and not visited[tx][ty]:
                visited[tx][ty] = True
                q.append((tx,ty))
                pos_score += 1 # 가능한 칸수 추가
    # print(now_board*pos_score)
    total_score += now_board*pos_score
   
    # a 주사위 아랫면 / b 주사위가 있는 칸 수 비교하여 이동 결정
    if bottom > now_board:
        now_di = (now_di + 1)%4
    elif bottom < now_board:
        now_di = now_di - 1
        if now_di < 0:
            now_di += 4
    
    x, y = ox, oy

print(total_score)


    