# ~ 11:15 1시간30분

'''
복제 마법
1. 복제마법. 
2. 모든 물고기가 한칸이동
상어, 냄새 있는칸 이동불가. 이동할수있을때까지 물고기는 45 반시계 회전함.
좌부터 1,2,3,4,5,6,7,8 로 시계방향. 하지만 회전은 반시계이다(역)
3. 상어 연속해서 세칸이동. 상어는 상하좌우로만. 무조건 세칸이동임. 
  이동방법은 사전순으로 상1 좌2 하3 우4 이며 큰수가 우선이다.
  물고기 있는 칸으로 이동하면 모든 물고기는 없어지며 냄새를 남김.
  이동 방법은 제외되는 물고기의 수가 가장 많은 방향으로 이동. 
4. 세번째 연습에서는, 첫번째에 생긴 냄새가 없어진다. 
S번의 연습을 마친 후 격자에 있는 물고기의 수를 출력한다.
'''
import time
t0 = time.time()
# 물고기수 m, 연습횟수 s
# m, s = map(int, input().split())

# fish = []
# for _ in range(m):
#     fish.append(tuple(map(int, input().split())))

m, s = 5, 26
fish = [ (4, 3, 5),
(1, 3, 5),
(2, 4, 2),
(2, 1, 6),
(3, 4, 4) ]
sx, sy = 4, 2




# 상어 처음위치
# sx, sy = map(int, input().split())


########
# 1. 물고기의 이동 구현
dx = (0,-1,-1,-1,0,1,1,1)
dy = (-1,-1,0,1,1,1,0,-1)



def fish_move():
    global fish
    fish_temp = []
    for fx,fy,d in fish:

        
        # 상어/피가 d방향 앞에 있다면, 이동불가하므로 회전, 아니면 이동
        for i in range(8):
            nx, ny = fx+dx[d-1], fy+dy[d-1]
            if nx < 1 or ny < 1 or nx > 4 or ny > 4 \
                or (nx,ny) == (sx,sy) or (nx,ny) in [(i[0],i[1]) for i in blood]:
                d -= 1
            else:
                break
        
        if d <= 0:
            d += 8

        if i == 7: # 다시 자기자신방향으로 돌아온경우
            fish_temp.append((fx,fy,d))
        else:
            # 이동한 좌표 및 방향 삽입
            fish_temp.append((nx,ny,d))
    fish = [i for i in fish_temp]
## 물고기 한칸이동 구현완료



### 2. 상어의 3칸이동 구현
# dfs 로 물고기 많은거 찾기

cx = (-1,0,1,0) # 상좌하우
cy = (0,-1,0,1)

'''
상상상, 상상하 등으로 이동. 
왔다갔다 해도 되는데 없앤 물고기는 없애지 않아야한다. 방문처리 필요.

'''


def shark_path(x,y,visited,eaten,path_tmp): # depth 0 visited = [(sx,sy)] eaten 0 path_tmp=[]
    global fish, path, max_eaten
    
    if len(path_tmp) == 3:
        # print('path_tmp, eaten:', path_tmp, eaten)
        # eaten 비교해서 크면 배열을 남긴다. 
        if max_eaten == 0 and not path:
            path = [p for p in path_tmp]
        
        if eaten > max_eaten:
            max_eaten = eaten
            path = [p for p in path_tmp]
            # print('eat:', path, max_eaten)
        return 
    
    for i in range(4):
        nx = x + cx[i]
        ny = y + cy[i]     
        if nx > 0 and ny > 0 and nx <= 4 and ny <= 4:
            if (nx,ny) not in visited: # 새 자리인경우
                next_eaten = eaten
                # print('not visit:', (nx,ny))
                for fx, fy, _ in fish:  # 물고기 있는 경우 먹어치움
                    if (nx,ny) == (fx,fy):
                        next_eaten += 1
                visited.append((nx,ny))    # 방문처리
                shark_path(nx,ny,visited,next_eaten,path_tmp+[i])  
                visited.remove((nx,ny))
            else: # 구 자리인경우
                shark_path(nx,ny,visited,eaten,path_tmp+[i]) 
             
    return 


def shark_move(): # path 따라 이동하고, 물고기 먹고, 피 남긴다
    global fish, sx, sy, blood
    fish_temp = [f for f in fish]
    for i in path: #0,1,2,3
        sx += cx[i]
        sy += cy[i]
        # 물고기 먹기
        for fx, fy, d in fish:
            if (sx,sy) == (fx,fy):
                fish_temp.remove((fx,fy,d)) 
                blood.append((fx,fy,stage))
    fish = [f for f in fish_temp]
    blood = list(set(blood))
            
    

### 시뮬레이션 실행 및 최종 물고기 수 출력
## test
print('start')
stage = 0
blood = []
for _ in range(s):
    path = []
    max_eaten = 0

    # 원래 상태 저장
    orgFish = [f for f in fish]
    fish_move()
    # print('fish move:')
    # for f in sorted(fish):
    #     print(f)

    shark_path(sx,sy,[(sx,sy)],0,[])
    shark_move()

    # print('path:',path)

    # blood 없애기
    rm_stage = stage - 2
    for bx, by, bs in blood:
        if bs == rm_stage:
            blood.remove((bx,by,bs))

    ### 3. 복제 
    for orf in orgFish:
        fish.append(orf)
    # print('stage:', stage)
    # print('fish:')
    # for f in sorted(fish):
    #     print(f)
    # print('blood:', blood)
    # print('shark:', (sx,sy))
    stage += 1

    # print('='*30)
print(len(fish))


print(time.time() - t0)

    
    

    

