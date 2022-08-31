# ~ 11:30 ~12:00
# 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.
n, m = 4, 6
board = [
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 6, 0],
[0, 0, 0, 0, 0, 0]
]

# cctv 방향마다 사각지대 구해서 최솟값 리턴
dx = (-1, 0, 1, 0) # 상우하좌 시계방향
dy = (0, 1, 0, -1)

# cctv 방향? 1,2,3,4,5  
# 상 부터 0,1,2,3 으로 시계방향으로 설정
cams = [None, [0], [1,3], [0,1], [0,1,2], [0,1,2,3]]
# 1, 3, 4 번은 4가지 가능. 2번은 2가지 가능, 5번은 1가지
# -1로 감시영역을 바꾸고 남은 0의 개수를 세면 됨.

def surv(x, y, di): # 감시 영역 -1로 바꾸는 함수
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

# 카메라마다 방향 정해줘서 완전탐색 수행
# cams의 방향을 계속 변경 - dfs, 첫번째가 다시 [0]이면 중단

def find_zero():
    # for x in range(n):
    #     for y in range(m):
    #         if 0 < room[x][y] < 6: # 카메라 찾은경우
    #             cnum = room[x][y] 
    #             for direc in cams[cnum]:
    #                 surv(x, y, direc)
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


org_cam_list = find_cams()
cam_list = [c[:] for c in org_cam_list]
min_dark = int(1e9)

print(cam_list)

''' 
(x,y,1,0), (x,y,3,0), (x,y,4,0) 
숫자에 맞게 회전시키고 dfs 로 ?  혹은 while
맨끝부터 조건에 맞게 1씩 증가시키고, 원래로 돌아오면 앞에것을 1씩 증가시킨다.
만약 처음으로 돌아오면 종료시킨다. 
'''
while True:
    # 맨처음거 방향 증가
    cam_list[0][-1] += 1
    cam_list[0][-1] == 
    for i in range(1, len(cam_list)): 
    # 앞이 0이 되면 1을 증가시키기
        if cam_list[i-1][-1] == 0:
            cam_list[i][-1] += 1
            # 3,4의 경우 // 4, 2인 경우 // 2
            if 3 <= cam_list[i][-2] < 4: 
                cam_list[i][-1] //= 4
            elif cam_list[i][-2] == 2:
                cam_list[i][-1] //= 2
    print(cam_list)
    if cam_list == org_cam_list: # 같아지면 모든 방법을 다 이용했으므로
        print('same')
        break

    room = [b[:] for b in board]

    for (x, y), cam_num, di in cam_list:
        if cam_num == 2:
            cam_dir = [c + di for c in cams[cam_num]]
        elif cam_num != 5:
            cam_dir = [(c + di) // 4 for c in cams[cam_num]]
        else:
            cam_dir = cams[cam_num]
        for di in cam_dir: 
            surv(x, y, di)

    # find zero
    dark = find_zero()
    if min_dark > dark:
        min_dark = dark

    # loop check
    for r in room:
        print(r)


print(min_dark)


        
        
        
