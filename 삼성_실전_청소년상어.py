# ~ 4:00
'''
물고기 번호 1~16. 한칸에 하나 씩 존재
같은번호 없음.
방향 8가지
0,0에 먼저 상어가 들어가 물고기 먹음. 
상어의 방향은 먹은 물고기와 같고, 물고기가 이후 이동

물고기 이동:
번호 작은 물고기부터 순서대로. 한칸 이동. 빈칸 및 다른 물고기 칸. 
상어 및 범위 벗어나면 X
반시계 회전으로 방향 전환
물고기 이동할때 서로의 위치를 바꿈. 바뀐 물고기의 방향은?

이후 상어 이동:
방향대로 이동하고 여러 칸을 갈수있음.
물고기 먹고, 물고기의 방향을 가짐. 
지나가는 칸에 있으면 물고기 먹지않음.
물고기 없으면 이동불가.
최종 : 이동 못하면 종료
상어가 이동 후에는 다시 물고기 이동. 반복.

답 : 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
'''
import copy
fish = [[] for _ in range(4)]


for j in range(4):
    board = list(map(int, input().split()))
    for i in range(4):
        fish[j].append([board[i*2], board[i*2+1]-1]) # 방향은 0~7


# board = [
# [7, 6, 2, 3, 15, 6, 9, 8],
# [3, 1, 1, 8, 14, 7, 10, 1],
# [6, 1, 13, 6, 4, 3, 11, 4],
# [16, 1, 8, 7, 5, 2, 12, 2]
# ]

for j in range(4):
    for i in range(4):
        fish[j].append([board[j][i*2], board[j][i*2+1]-1])
    

# print('init')
# for f in fish:
#     print(f)

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

belly_max = []
def dfs(fish, sx, sy, belly):
    # 상어가 처음에 물고기를 먹는다.
    belly_after = belly + fish[sx][sy][0]
    fish[sx][sy][0] = 0

    # 물고기 순서대로 찾고, 하나씩 이동하기
    
    for num in range(1,17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if fish[x][y][0] == num:
                    fx, fy = x, y
        if (fx, fy) != (-1,-1):
            # 물고기 이동
            # 방향 맞을때까지 위치 바꿈
            fd = fish[fx][fy][1]
            for _ in range(8):
                nx = fx + dx[fd]
                ny = fy + dy[fd]
                if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or \
                    (nx,ny) == (sx,sy):
                    fd += 1
                    if fd == 8:
                        fd = 0
                else:
                    fish[fx][fy][1] = fd
                    fish[fx][fy], fish[nx][ny] = fish[nx][ny], fish[fx][fy]
                    break
                    
            # 물고기 마다 이동 결과 출력
            # print('fish num:',num)
            # for f in fish:
            #     print(f)


    # # test 출력
    # print((sx,sy))
    # print('eat, fish moved')
    # for f in fish:
    #     print(f)
    # 상어 이동 - 초기 조건이 이후 이동과 같은 방식이므로 따로 초기 조건을 구현하지는 않는다.
    # 상어칸의 물고기 0 -> 상어 이동 -> 
    
    sd = fish[sx][sy][1]
    
    moved = False
    for l in range(1,4):
        snx, sny = sx+l*dx[sd], sy+l*dy[sd]
        
        # print('shark move')
        # print(l)
        # print(snx,sny)

        if (0 <= snx < 4) and (0 <= sny < 4) and fish[snx][sny][0] > 0:
            # print('shark moved', (snx,sny))
            moved = True
            
            # for f in fish:
            #     print(f)

            # new_fish = [f[:] for f in fish]
            # print('new_fish', new_fish)
            # print(id(fish[0][0]), id(new_fish[0][0]))
            # dfs(new_fish, snx, sny, belly_after)
            dfs(copy.deepcopy(fish), snx, sny, belly_after)
            
    if not moved:
        # print('not moved')
        # global belly_max
        belly_max.append(belly_after)
             

dfs(fish, 0, 0, 0)
# print(belly_max)
print(max(belly_max))
