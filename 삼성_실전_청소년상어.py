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

# fish = []
# for _ in range(4):
#     fish.append(list(map(int, input().split())))

fish = [ 
[7, 6, 2, 3, 15, 6, 9, 8],
[3, 1, 1, 8, 14, 7, 10, 1],
[6, 1, 13, 6, 4, 3, 11, 4],
[16, 1, 8, 7, 5, 2, 12, 2]
]


new_fish = [[] for _ in range(4)]
fish_ext = []
for x in range(4):
    for y in range(4):
        ai = fish[x][y*2]
        bi = fish[x][y*2+1] 
        new_fish[x].append([ai,bi-1])
        fish_ext.append([ai,bi-1])

dir_fish = [None]
fish_ext = sorted(fish_ext)

for _,y in fish_ext:
    dir_fish.append(y)

fish = [n[:] for n in new_fish]





def init_shark():
    global belly, surv_fish, shark_d
    belly += fish[0][0][0]
    surv_fish.remove(fish[0][0][0])
    dir_fish[fish[0][0][0]] = None
    fish[0][0][0] = -1
    shark_d = fish[0][0][1]

def find_fish(num,fish):
    for x in range(4):
        for y in range(4):
            if fish[x][y][0] == num:
                return x,y

def fish_move(fish, surv_fish, dir_fish, sx, sy):
            # 이전 어항, 있는 물고기 목록([[]]), 있는 물고기방향([[]]), 상어위치( [ ,])
    # global fish
    new_fish = [f[:] for f in fish]
    new_dir_fish = [d for d in dir_fish]
    for num in surv_fish: # 
        x, y = find_fish(num,new_fish) # 물고기 찾고 이동가능 확인
        d = dir_fish[num] # 0~7
        # print('x,y,d: ',(x,y,d))
        for di in range(8):
            nx,ny = x+dx[d], y+dy[d]
            # print('nxny:', (nx,ny))
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4\
                or (nx,ny) == (sx,sy):
                # print('no. change dir')
                d += 1
                if d == 8:
                    d = 0
            else:
                break
        
        if di < 7:
            # fish 방향 수정
            new_dir_fish[num] = d
            new_fish[x][y][1] = d
            # swap
            new_fish[nx][ny], new_fish[x][y] = new_fish[x][y], new_fish[nx][ny]
    return new_fish, new_dir_fish

   
def shark_move(osx,osy, sd, shark_belly, fish, surv_fish, dir_fish):
    # 처음 상어 위치 저장
    isx, isy = osx, osy
    # 물고기 이동
    moved_fish, moved_dir_fish = fish_move(fish, surv_fish, dir_fish, osx,osy)
    
    print('fish moved')
    for f in moved_fish:
        print(f) 
    
    print(moved_dir_fish)
    print(surv_fish)
    # 상어 이동. 재귀
    moved = False
    for i in range(1,4): # 한칸, 두칸, 세칸
        
        sx = osx + i*dx[sd]
        sy = osy + i*dy[sd]
        print(sx,sy)
        if sx >= 0 and sy >= 0 and sx < 4 and sy < 4 and \
            moved_fish[sx][sy][0] > 0: # 물고기 있어야 이동.
            moved = True

            print('before shark moved')
            for f in moved_fish:
                print(f)
            # 경우따라 달리 가야하므로 fish 복제
            new_fish = [f[:] for f in moved_fish]
            new_surv_fish = [s for s in surv_fish]
            new_dir_fish = [d for d in moved_dir_fish]

            # 이동해서 잡아먹고 방향바꿈
            # 원래 위치에는 먹었으므로 0을 남김
            new_fish[isx][isy][0] = 0

            # 먹힌 물고기 제거, 방향도 제거
            df, dd = new_fish[sx][sy] # 먹힌 물고기 번호, 방향
            new_surv_fish.remove(df)
            new_dir_fish[df] = None

            new_fish[sx][sy][0] = -1 # 상어위치는 -1로 표기
            # sd = dd # 상어 방향은 먹힌 물고기의 방향

            # 먹힌 물고기 숫자를 belly 에 더함
            shark_belly_after = shark_belly + df

            ## 중간결과 print
            print('shark moved')
            for f in new_fish:
                print(f)
            print('='*30)
            # print(isx, isy)
            # print(sx,sy)
            # print(sd)
            # print(new_surv_fish)
            # print(new_dir_fish)
            
            # 재귀함수 실행
            shark_move(sx,sy,dd,shark_belly_after,\
                new_fish,new_surv_fish,new_dir_fish)
    
    # 상어 안움직일 경우
    if not moved:
        print('cannot move')
        # 먹은 거 cand 추가하고 return
        print('belly:', shark_belly)
        eaten_cand.append(shark_belly)
        
        

    

                

            

        
        
        



### test 
dx = (-1,-1,0,1,1,1,0,-1)
dy = (0,-1,-1,-1,0,1,1,1)
sx,sy = 0,0
shark_d = -1
belly = 0
eaten_cand = [] 
surv_fish = list(range(1,17))

init_shark()
# for n in fish:
#     print(n)
# fish, dir_fish = fish_move(fish, surv_fish, dir_fish, sx, sy)
# print(surv_fish)
# print(dir_fish)
print(sx, sy, belly, surv_fish, dir_fish)
print('phase 0:')
for f in fish:
    print(f)

shark_move(sx, sy, shark_d, belly, fish, surv_fish, dir_fish)

print(max(eaten_cand))

