from collections import deque

# n = 3
# cost = [ 
#     [5,5,4],
#     [3,9,1],
#     [3,2,7]
# ]

# n = 5
# cost = [ 
#     [3, 7, 2, 0, 1],
#     [2, 8, 0, 9, 1],
#     [1, 2, 1, 8, 1],
#     [9, 8, 9, 2, 0],
#     [3, 6, 5, 1, 5]
# ]

n = 7
cost = [ 
    [9,0,5,1,1,5,3],
    [4,1,2,1,6,5,3],
    [0,7,6,1,6,8,5],
    [1,1,7,8,3,2,3],
    [9,4,0,7,6,4,1],
    [5,8,3,2,4,8,3],
    [7,4,8,4,8,3,4]
]

# 최단거리 - 다익스트라 0,0 ~ n-1, n-1 
# dfs 로 되지 않나? !! dfs 로 하면 시간 부족.
dx = (1,0,-1,0) # 하우
dy = (0,1,0,-1)

dist_cand = []
visited = [[False]*n for _ in range(n)]
def dfs(x, y, distance, visited):
    if x > n-1 or y > n-1 or x < 0 or y < 0 or visited[x][y]:
        return
    else:
        distance += cost[x][y]
        if x == n-1 and y == n-1:
            dist_cand.append(distance) 
            return
        else:
            for i in range(4):
                visited[x][y] = True
                dfs(x+dx[i], y+dy[i], distance, visited)
                visited[x][y] = False
        
            
dfs(0,0,0, visited)
print(dist_cand)
print(min(dist_cand))

