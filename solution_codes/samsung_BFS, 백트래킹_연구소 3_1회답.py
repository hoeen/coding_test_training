# 11:45 시작 ~12:20 35분  거의 2시간 걸려서 품.
from collections import deque

# 모든 2를 찾아서 그 중 M개를 활성화. 
def find_virus():
    vpos_list = []
    for x in range(n):
        for y in range(n):
            if lab[x][y] == 2:
                vpos_list.append((x, y, 0))
    return vpos_list 

# 활성화한 바이러스가 퍼지는것 구현
# 활성화 된곳마다 퍼지면서 같거나 작은 숫자 있으면 놔두고, 더 큰 숫자면 덮어씀. 
# BFS
def activate(spread, lab, x, y, t): 
    # global spread, lab
    spread, lab = [s[:] for s in spread], [l[:] for l in lab]
    q = deque([])
    visited = [[False]*n for _ in range(n)]
    q.append((x, y))
    visited[x][y] = True
    lab[x][y] = 3 # 활성화 표시
    if spread[x][y] > t:
        spread[x][y] = t

    more_virus = [] # 퍼짐으로서 더 활성화되는 바이러스

    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and lab[nx][ny] != 1:
                    if spread[nx][ny] == 0 or spread[nx][ny] > spread[qx][qy] + 1:
                # min(spread[nx][ny], spread[qx][qy]) in [0, spread[qx][qy]]:
                        visited[nx][ny] = True
                        spread[nx][ny] = spread[qx][qy] + 1
                        q.append((nx, ny))
                        # break
                        # 활성화 안된 바이러스 찾으면 - 활성화하여 3으로 지정하고 퍼진 시간과 같이 리스트 추가
                        if lab[nx][ny] == 2:
                            lab[nx][ny] = 3
                            more_virus.append((nx, ny, spread[nx][ny]))


    return spread, lab, more_virus

# 전체 spread 에서 0이 모두 벽인지 체크, 그럴 경우 숫자 중 최댓값 반환
def check(lab, spread):
    global min_time
    elapsed = 0
    for x in range(n):
        for y in range(n):
            if spread[x][y] > elapsed and lab[x][y] == 0:
                elapsed = spread[x][y]
            if spread[x][y] == 0 and lab[x][y] == 0:
                return # 감염 안 퍼진 빈칸 존재
    
    if elapsed < min_time:
        min_time = elapsed            

# 활성화 하고 다음것 진행 / 활성화 안하고 다음것 진행 방식으로 완전탐색
def dfs(lab, spread, vpos_list, count):
    if len(vpos_list) == 0 or count == m:  
        check(lab, spread) # 체크하고 최솟값 갱신
        return
    
    vx, vy, vt = vpos_list[0]
    new_spread, new_lab, more_virus = activate(spread, lab, vx, vy, vt)

    # 더 활성화된 바이러스 있으면 활성화 진행
    while more_virus:
        mx, my, mt = more_virus.pop(0)
        new_spread, new_lab, mv = activate(new_spread, new_lab, mx, my, mt)
        for i in mv:
            more_virus.append(i)            

    dfs(new_lab, new_spread, vpos_list[1:], count+1)
    dfs([l[:] for l in lab], [s[:] for s in spread], vpos_list[1:], count)
    

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
spread = [[0]*n for _ in range(n)]

dx = (-1, 0, 0, 1) # 상 우 좌 하 시계방향
dy = (0, 1, -1, 0)

min_time = int(1e9)

vpos_list = find_virus()

dfs(lab, spread, vpos_list, 0)

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)



