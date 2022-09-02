# 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# cctv 방향마다 사각지대 구해서 최솟값 리턴
dx = (-1, 0, 1, 0) # 상우하좌 시계방향
dy = (0, 1, 0, -1)

# 상 부터 0,1,2,3 으로 시계방향으로 설정
cams = [None, [0], [0,2], [0,1], [0,1,2], [0,1,2,3]]
# -1로 감시영역을 바꾸고 남은 0의 개수를 세면 됨.

def surv(x, y, di, room): # 감시 영역 -1로 바꾸는 함수
    nx, ny = x + dx[di], y + dy[di] # 방향따라 한칸 이동
    while (0 <= nx < n) and (0 <= ny < m) \
        and room[nx][ny] != 6:
        # 0면 -1로 바꾸기 전진 가능
        if room[nx][ny] == 0:
            room[nx][ny] = -1
        # 1,2,3,4,5,-1인경우: 건너뛰기
        # 한칸 전진
        nx, ny = nx + dx[di], ny + dy[di]
    return

def find_zero(room):
    count = 0 
    for x in range(n):
        for y in range(m):
            if room[x][y] == 0:
                count += 1
    return count

def find_cams():
    cam_list = []
    for x in range(n):
        for y in range(m):
            if 0 < board[x][y] < 6:
                cam_list.append([(x,y),board[x][y],0]) #(위치), 값, 방향 0
    return cam_list

cam_list = find_cams()
min_dark = find_zero(board)

# 카메라마다 방향 정해줘서 완전탐색 수행
# dfs
''' 
(x,y,1,0), (x,y,3,0), (x,y,4,0) 
숫자에 맞게 회전시키고 dfs 로 ?  혹은 while
맨끝부터 조건에 맞게 1씩 증가시키고, 원래로 돌아오면 앞에것을 1씩 증가시킨다.
만약 처음으로 돌아오면 종료시킨다. 
'''
def dfs(cam_list, ind):
    global min_dark
    room = [b[:] for b in board]
    
    # 현재 상태에서 감시 영역 체크
    for (x, y), cam_num, di in cam_list:
        cam_dir = [(c + di) % 4 for c in cams[cam_num]]
        for di in cam_dir: 
            surv(x, y, di, room)

    # find zero
    dark = find_zero(room)
    if min_dark > dark:
        min_dark = dark

    new1_cam_list = [c[:] for c in cam_list]
    if ind < len(cam_list) - 1:
        dfs(new1_cam_list, ind+1) # 재귀1 : 다음 cam으로 넘김

    # 재귀2 : 현재 cam 방향 돌리기
    cam_list[ind][-1] += 1
    cam_list[ind][-1] %= 4

    # 다시 0으로 돌아온다면 종료
    if cam_list[ind][-1] == 0:
        return
    
    new2_cam_list = [c[:] for c in cam_list]    
    dfs(new2_cam_list, ind)

if cam_list:
    dfs(cam_list, 0)

print(min_dark)