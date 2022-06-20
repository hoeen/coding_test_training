# ~3:00  / ~3:30    # 끝낸시간 - 4:37 총 2시간 7분 걸림..
'''
사과 먹으면 길이 늘어남. 벽 또는 자기 몸과 부딪히면 끝남
N,N 보드 . 
뱀 길이 처음에 1. (0,0)에 위치.
첨에 오른쪽을 향함.
다음과 같은 규칙으로 매초마다 이동
> 몸길이 늘어나 다음칸으로 위치
> 사과 있으면 사과 없어지고 꼬리는 안움직
> 사과 없으면 몸길이 줄여서 꼬리 위치칸을 비워줌. 몸길이는 원래대로 

이때, 사과 위치와 뱀 이동경로 주어질때 게임이 몇 초에 끝나는지 계산하기.

1. 크기 n, 사과 개수 k
2. k개 줄에 사과 위치. (x,y). (0,0)에는 사과 없음
3. 다음 줄에는 방향 변환 횟수 L 주어짐
4. 다음 L개 줄에는 방향변환 정보. 정수와 문자 C. X초가 끝난 뒤에 왼쪽 90 (L) 혹은 
오른쪽 90(D)로 회전. 
'''

n = int(input())
k = int(input())

# 기본맵 - nxn 0으로 구성
board = [[[0, None] for _ in range(n)] for _ in range(n)]

# 사과위치 - 2로 표시
for i in range(k):
    ax, ay = map(int,input().split())
    board[ax-1][ay-1] = [2, None]

# 방향 변환 횟수
l = int(input())

# 방향 변환 큐 생성
q = list()
for j in range(l):
    t, c = input().split() 
    q.append((int(t), c))

## 뱀의 움직임 구현
# 좌 상 우 하
dx = [0,-1,0,1]
dy = [-1,0,1,0]

# L이면 역으로 이동. D이면 순으로 이동
di = 2 # 처음은 우

# 첫 위치 : 0,0
x, y = (0, 0) # 머리
tx, ty = (0, 0) # 꼬리

# 첫 시간 0
second = 0

# 첫 방향 설정하여 board에 넣어줌
board[x][y] = [1,di] # 뱀 여부, 방향 인덱스 

# second 증가시키면서, second가 부합하면 방향 바꿈
while -1 < x and x < n and -1 < y and y < n:
    second += 1
    
    # 방향 아직 안바꿀때:
    # 방향 앞으로 이동하고 사과 확인

    # 머리가 인덱스 벗어나면 종료. 1 만나면 종료. 증가한 초 반환
    if x+dx[di] < 0 or x+dx[di] >= n or y+dy[di] < 0 or y+dy[di] >= n:
        print(second)
        break 

    elif board[x+dx[di]][y+dy[di]][0] == 1:
        print(second)
        break

    else:
        if board[x+dx[di]][y+dy[di]][0] != 2: # 사과 없을때
            # 머리 이동. 방향 남김
            board[x][y][1] = di # 만약 방향 바뀌었을시 꼬리에게 알려줄 정보 남김.
            x, y = (x+dx[di], y+dy[di])
            board[x][y] = [1,di]
            # 꼬리 존재한 칸 삭제 후 방향따라 이동
            tdi = board[tx][ty][1]
            board[tx][ty] = [0, None]
            tx += dx[tdi]
            ty += dy[tdi]
            
            
        else: # 사과 있을때
            # 머리 이동. 방향 남김
            board[x][y][1] = di # 만약 방향 바뀌었을시 꼬리에게 알려줄 정보 남김.
            x, y = (x+dx[di], y+dy[di])
            board[x][y] = [1,di]
            # 꼬리는 한번 쉰다.
            


    # 다음 방향변환 초 및 방향 검색
    if q:
        t, c = q[0]
    if second == t:
        t, c = q.pop(0)
        # 방향변환 초 됐을때는 방향 바꿈
        if c == 'L':
            di -= 1
            if di < 0:
                di += 4

        else: # c == 'D':
            di += 1
            di = di%4
        


