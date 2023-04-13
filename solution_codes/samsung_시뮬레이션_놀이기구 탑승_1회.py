''' 
로직 순서:
1. for x : for y 로 접근
2. 비어있는 칸 세기 / 인접 좋아하는 친구 세기
3. (좋아하는 친구, 비어있는 칸, x, y)로 정렬. 많 많 적 적 이 중 첫번째로 이동 
''' 
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def place(id):
    global board
    cand = []
    for x in range(n):
        for y in range(n):
            empty = 0
            friends = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == 0:
                        empty += 1
                    elif board[nx][ny] in graph[id]:
                        friends += 1
            cand.append((friends, empty, x, y))
    cand.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    
    # 그자리가 빈칸 아니면 넘어감
    for c in range(len(cand)):
        f, e, cx, cy = cand[c]
        if board[cx][cy]: # 빈칸 아니면
            continue
        else:
            board[cx][cy] = id
            break
    return


n = int(input())
graph = [None for _ in range(n*n+1)] # 0~n까지의 학생
seq = []

for _ in range(n*n):
    n0, n1, n2, n3, n4 = list(map(int, input().split()))
    graph[n0] = [n1, n2, n3, n4]
    seq.append(n0)

board = [[0]*n for _ in range(n)] # nxn 0은 빈칸

for id in seq:
    place(id)
    
score = 0
score_board = [0,1,10,100,1000]
# 인접한 친구에 따라 점수 부여
for x in range(n):
    for y in range(n):
        friends = 0
        st = board[x][y]
        if not st:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in graph[st]:
                    friends += 1
            
        score += score_board[friends]

print(score)