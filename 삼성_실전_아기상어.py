# ~1:35  # 총 걸린시간 3시간 19분
n = int(input())

ocean = []
for _ in range(n):
    ocean.append(list(map(int,input().split())))

# ocean = [ 
#     [0,0,0],
#     [0,0,0],
#     [0,9,0]
# ]

# ocean = [ 
#     [4,3,2,1],
#     [0,0,0,0],
#     [0,0,9,0],
#     [1,2,3,4]
# ]

# ocean = [ 
#     [5,4,3,2,3,4],
#     [4,3,2,3,4,5],
#     [3,2,9,5,6,6],
#     [2,1,2,3,4,5],
#     [3,2,1,6,5,4],
#     [6,6,6,6,6,6]
# ]

# ocean = [ 
#     [6,0,6,0,6,1],
#     [0,0,0,0,0,2],
#     [2,3,4,5,6,6],
#     [0,0,0,0,0,2],
#     [0,2,0,0,0,0],
#     [3,9,3,0,0,1]
# ]
# ocean = [ 
#     [1,1,1,1,1,1],
#     [2,2,6,2,2,3],
#     [2,2,5,2,2,3],
#     [2,2,2,4,6,3],
#     [0,0,0,0,0,6],
#     [0,0,0,0,0,9]
# ]


def find_shark():
    for x in range(n):
        for y in range(n):
            if ocean[x][y] == 9:
                return (x,y)






shark = 2 # 상어 크기
ate = 0 # 먹은수
time = 0

dx = (-1,0,0,1) # 먹는순서 중요! 가장 위부터 탐색, 그리고 왼쪽부터 탐색. 상좌우하
dy = (0,-1,1,0)

def bfs():
    global shark, ate
    q = list()
    visited = [[-1]*n for _ in range(n)]
    init = find_shark()
    dist = 0

    q.append(init)
    visited[init[0]][init[1]] = 0 # 첫 방문처리를 시간으로 함. 걸린 시간 0
    ocean[init[0]][init[1]] = 0 # 상어 뺌
    '''
    q에 출발점 넣고, 하나씩 빼면서 찾은것들을 q에 삽입. 
    통과 못할 경우? visited에는 넣고, q에는 안넣는다.
    '''

    while q:
        x, y = q.pop(0)
        # 상하좌우 탐색

        for i in range(4):
            qx, qy = x + dx[i], y + dy[i]
            if qx < 0 or qy < 0 or qx >= n or qy >= n:
                continue
            else:
                if visited[qx][qy] >= 0:
                    continue
                else:
                    if ocean[qx][qy] > shark : # 크기 큰경우, visited에만 넣고 q에는 안넣음
                        visited[qx][qy] = visited[x][y] + 1
                    elif ocean[qx][qy] == shark: # 크기 같은경우 방문하나 먹지못함
                        visited[qx][qy] = visited[x][y] + 1
                        q.append((qx,qy))
                    elif ocean[qx][qy] > 0: # 크기 작으면 - 거리정보 저장. 나중에 거리 같은것끼리 위치 비교
                        if not dist:
                            dist = visited[x][y] + 1
                        visited[qx][qy] = visited[x][y] + 1

                        
                    else: # 그냥 빈공간
                        visited[qx][qy] = visited[x][y] + 1
                        q.append((qx,qy))

    # 먹을것들 정렬해서 첫번째거 먹고 업데이트, 그후 리턴
    eat_cand = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == dist and ocean[i][j] > 0 and ocean[i][j] < shark:
                eat_cand.append((i,j))
    if eat_cand:
        qx, qy = sorted(eat_cand)[0]
        q.append((qx,qy))

        # 먹었으니 상어로 대치
        ocean[init[0]][init[1]] = 0
        ocean[qx][qy] = 9 

        ate += 1
        if ate == shark:
            shark += 1  # 상어 상태 업데이트
            ate = 0
        return visited[qx][qy]

    return -1
           
        

# print(bfs())
# print(bfs())
# for o in ocean:
#     print(o)

# -1 나올때까지 bfs 반복실행
# -1 나오면 그동안 추가한 시간 반환  
for i in range(3000):
    res = bfs()
    # print(i+1, '='*30)
    # for o in ocean:
    #     print(o)
    # print(shark, ate)
    
    if res != -1:
        time += res
        # print('time elapsed:', time)
    else:
        print(time)
        break
        