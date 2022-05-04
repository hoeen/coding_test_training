'''
(x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승하게 된다. 
같은 온풍기에서 나온 바람이 여러 번 도착한다고 해도 온도는 여러번 상승하지 않는다.

온도가 높은 칸에서 낮은 칸으로 ⌊(두 칸의 온도의 차이)/4⌋만큼 온도가 조절된다. 
높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승한다.  벽이 있는 경우에는 온도가 조절되지 않는다.

1. 바람나옴
2. 온도조절
3. 온도 1 이상인 벽쪽 온도가 1씩 감소
4. 초콜릿
5. 모든 칸온도가 K 이상인지 검사.  맞다면 테스트 끝. 아니면 1부터 다시 반복.

'''
import sys
input = sys.stdin.readline

# r,c 보드 크기, 조사하는 온도 K
# r,c,k = map(int, input().split()) 

# 방 정보 기입
# room = []
# for _ in range(r):
#     room.append(list(map(int, input().split())))

# # 벽 개수
# w = int(input())
# wall = []
# for _ in range(w):
#     wall.append(tuple(map(int, input().split())))


r,c,k = 7,8,100
room = [ 
    [0,0,0,0,0,0,5,0],
    [5,4,4,4,4,4,4,0],
    [0]*8,
    [0,0,5,5,0,0,0,0],
    [0,0,0,0,0,5,0,0],
    [5,0,0,0,0,0,5,0],
    [0,0,0,0,3,0,0,0],
]

w = 3
wall = [(4,4,1),
(5,4,0),
(5,6,0)]

# wall 좌표에 맞게 바꾸기
wall = [(wa[0]-1, wa[1]-1, wa[2]) for wa in wall]

## 1. 팬 찾기
def find_fan():
    fan_list = []
    for x in range(r):
        for y in range(c):
            if room[x][y] >= 1 and room[x][y] <= 4:
                fan_list.append((x,y,room[x][y]))
                room[x][y] = 0 # 방에서 숫자 없애기
    return fan_list

def find_check():
    check_list = []
    for x in range(r):
        for y in range(c):
            if room[x][y] == 5:
                check_list.append((x,y))
                room[x][y] = 0 # 방에서 숫자 없애기
    return check_list

# fan : (1,4,4), (6,4,3)
## 2. 바람 불고 합산
def wind_dfs(x,y,d,length,visited):  #length = 0 
    if d == 1: # 1 오 / 2 왼 / 3 위 / 4 아래
        if length == 0:
            x = x
            y += 1
            room[x][y] += 5
            visited[x][y] = True
            # 벽 조건 걸기
            if (x+1,y,1) not in wall and (x+1,y,0) not in wall:
                wind_dfs(x+1,
                 y+1, d, length+1,visited)
            if (x, y, 1) not in wall:
                wind_dfs(x,y+1, d, length+1,visited)
            if (x, y, 0) not in wall and (x-1,y,1) not in wall:
                wind_dfs(x-1,y+1, d, length+1,visited)
        else:
            if x >= 0 and y >= 0 and x < r and y < c:
                if not visited[x][y]:
                    if 5-length >= 0:
                        room[x][y] += 5-length
                        visited[x][y] = True
                        if (x+1,y,1) not in wall and (x+1,y,0) not in wall:
                            wind_dfs(x+1, y+1, d, length+1,visited)
                        if (x, y, 1) not in wall:
                            wind_dfs(x,y+1, d, length+1,visited)
                        if (x, y, 0) not in wall and (x-1,y,1) not in wall:
                            wind_dfs(x-1,y+1, d, length+1,visited)
    elif d == 2: # 왼
        if length == 0:
            x = x
            y -= 1
            room[x][y] += 5
            visited[x][y] = True
            if (x+1,y-1,1) not in wall and (x+1,y,0) not in wall:
                wind_dfs(x+1, y-1, d, length+1,visited)
            if (x,y-1,1) not in wall:
                wind_dfs(x,y-1, d, length+1,visited)
            if (x-1,y-1,1) not in wall and (x,y,0) not in wall:
                wind_dfs(x-1,y-1, d, length+1,visited)
        else:
            if x >= 0 and y >= 0 and x < r and y < c:
                if not visited[x][y]:
                    if 5-length >= 0:
                        room[x][y] += 5-length
                        visited[x][y] = True
                        if (x+1,y-1,1) not in wall and (x+1,y,0) not in wall:
                            wind_dfs(x+1, y-1, d, length+1,visited)
                        if (x,y-1,1) not in wall:
                            wind_dfs(x,y-1, d, length+1,visited)
                        if (x-1,y-1,1) not in wall and (x,y,0) not in wall:
                            wind_dfs(x-1,y-1, d, length+1,visited)
    
    elif d == 3:  # 위
        if length == 0:
            x -= 1
            y = y
            room[x][y] += 5
            visited[x][y] = True
            if (x,y+1,0) not in wall and (x,y,1) not in wall:
                wind_dfs(x-1, y+1, d, length+1,visited)
            if (x,y,0) not in wall:
                wind_dfs(x-1,y, d, length+1,visited)
            if (x,y-1,0) not in wall and (x,y-1,1) not in wall:
                wind_dfs(x-1,y-1, d, length+1,visited)
        else:
            if x >= 0 and y >= 0 and x < r and y < c:
                if not visited[x][y]:
                    if 5-length >= 0:
                        room[x][y] += 5-length
                        visited[x][y] = True
                        if (x,y+1,0) not in wall and (x,y,1) not in wall:
                            wind_dfs(x-1, y+1, d, length+1,visited)
                        if (x,y,0) not in wall:
                            wind_dfs(x-1,y, d, length+1,visited)
                        if (x,y-1,0) not in wall and (x,y-1,1) not in wall:
                            wind_dfs(x-1,y-1, d, length+1,visited)
    
    elif d == 4:  # 아래
        if length == 0:
            x += 1
            y = y
            room[x][y] += 5
            visited[x][y] = True
            if (x,y,1) not in wall and (x+1,y+1,0) not in wall:
                wind_dfs(x+1, y+1, d, length+1,visited)
            if (x+1,y,0) not in wall:
                wind_dfs(x+1,y, d, length+1,visited)
            if (x+1,y-1,0) not in wall and (x,y-1,1) not in wall:
                wind_dfs(x+1,y-1, d, length+1,visited)
        else:
            if x >= 0 and y >= 0 and x < r and y < c:
                if not visited[x][y]:
                    if 5-length >= 0:
                        room[x][y] += 5-length
                        visited[x][y] = True
                        if (x,y,1) not in wall and (x+1,y+1,0) not in wall:
                            wind_dfs(x+1, y+1, d, length+1,visited)
                        if (x+1,y,0) not in wall:
                            wind_dfs(x+1,y, d, length+1,visited)
                        if (x+1,y-1,0) not in wall and (x,y-1,1) not in wall:
                            wind_dfs(x+1,y-1, d, length+1,visited)

## 3. 온도조절
def control_temp():
    global room
    new_room = [[-1]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            near_list = [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]
            nw_list = [(x,y,0), (x,y-1,1), (x+1,y,0), (x,y,1)]
            # new room 에 원래 온도 넣기
            new_room[x][y] = room[x][y]
            
            # 벽 있는경우엔 넘어감
            for i in range(4):
                nx, ny = near_list[i]
                
                    
                if nx >= 0 and ny >= 0 and nx < r and ny < c:
                    if nw_list[i] not in wall:
                        rt = room[x][y]
                        nt = room[nx][ny]
                        diff = abs(rt-nt)//4
                        if rt < nt:
                            new_room[x][y] += diff
                            
                                
                        elif rt > nt:
                            new_room[x][y] -= diff
                            
                                

    room = [new[:] for new in new_room]
                    
## 4. 바깥쪽 온도 1도 감소
# 0, r-1, c-1
def edge_cool():
    for x in range(r):
        for y in range(c):
            if x == 0:
                if y != c-1:
                    if room[x][y] != 0:
                        room[x][y] -= 1
            if x == r-1:
                if y != 0:
                    if room[x][y] != 0:
                        room[x][y] -= 1
            if y == 0:
                if x != 0:
                    if room[x][y] != 0:
                        room[x][y] -= 1
            if y == c-1:
                if x != r-1:
                    if room[x][y] != 0:
                        room[x][y] -= 1
            
## 5. 조사하는 칸 온도 K 검사
def temp_check(checklist):
    ans = True
    for cx, cy in checklist:  # (x,y)
        if room[cx][cy] < k:
            ans = False
    return ans 
         
# 정답 도출
cho = 0
fan_list = find_fan()
check_list = find_check()
while True:
    for fx,fy,fd in fan_list:
        wind_dfs(fx,fy,fd,0,[[False]*c for _ in range(r)])
    control_temp()
    edge_cool()
    cho += 1
    if temp_check(check_list): # True 이면 중단, False이면 다시 시작
        print(cho)
        break
    if cho == 100:
        print(101)
        break

for ro in room:
    print(ro)


