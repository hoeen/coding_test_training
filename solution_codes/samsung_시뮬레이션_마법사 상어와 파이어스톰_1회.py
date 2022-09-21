# 10:30 ~ 11:30 1시간 4분

'''파이어스톰
단계 L 설정
2**L 정사각형으로 나눔. -> 90도 시계방향 회전
얼음이 있는 칸 2개 이하면 얼음 1 줄어듬.
'''

'''
Q 번 파이어스톰 시전
1. 남아있는 얼음 합
2. 가장 큰 덩어리가 차지하는 칸의 개수 - 얼음 연결의 집합
'''
def div_and_rotate(l):
    global board
    # 부분격자 나눔
    length = 2**l
    if length == 1:
        return
    for x in range(0, 2**n, length):
        for y in range(0, 2**n, length):
            part = [[None]*length for _ in range(length)]
            for xi in range(length):
                for yi in range(length):
                    part[xi][yi] = board[x+xi][y+yi]
            
            # 90도 시계방향 회전
            part_90 = list(zip(*part[::-1]))

            # 다시 board에 넣기
            for xi in range(length):
                for yi in range(length):
                    board[x+xi][y+yi] = part_90[xi][yi]
    

def near(): 
    # 인접한 얼음 조사해서 2개 이하면 1 줄이기 
    new_board = [b[:] for b in board]
    for x in range(2**n):
        for y in range(2**n):
            count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 2**n and 0 <= ny < 2**n:
                    if board[nx][ny] > 0:
                        count += 1
            if count <= 2:
                if board[x][y] > 0:
                    # print('minus 1. x,y :', (x, y))
                    new_board[x][y] -= 1
    return new_board

def bunch():
    # 가장 큰 덩어리의 칸 개수를 반환
    max_b = 0
    for x in range(2**n):
        for y in range(2**n):
            if board[x][y] > 0:
                q = [(x,y)]
                visited = [[False]*(2**n) for _ in range(2**n)]
                visited[x][y] = True
                ice = 1
                while q:
                    qx, qy = q.pop(0)
                    for i in range(4):
                        nx, ny = qx + dx[i], qy + dy[i]
                        if 0 <= nx < 2**n and 0 <= ny < 2**n:
                            if not visited[nx][ny] and board[nx][ny] > 0:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                ice += 1
                if max_b < ice:
                    max_b = ice
    
    return max_b



            
    


n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
skills = list(map(int, input().split()))
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for qi in range(q):
    # print('L:', skills[qi])
    div_and_rotate(skills[qi])
    
    # print('after rotate:')
    # for b in board:
    #     print(b)

    board = near()

    # print('after near:')
    # for b in board:
    #     print(b)

print(sum([sum(b) for b in board]))
print(bunch())