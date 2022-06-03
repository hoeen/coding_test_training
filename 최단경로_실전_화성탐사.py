n = 3
# cost = [ 
#     [5,5,4],
#     [3,9,1],
#     [3,2,7]
# ]

n = 5
cost = [ 
    [3, 7, 2, 0, 1],
    [2, 8, 0, 9, 1],
    [1, 2, 1, 8, 1],
    [9, 8, 9, 2, 0],
    [3, 6, 5, 1, 5]
]

# n = 7
# cost = [ 
#     [9,0,5,1,1,5,3],
#     [4,1,2,1,6,5,3],
#     [0,7,6,1,6,8,5],
#     [1,1,7,8,3,2,3],
#     [9,4,0,7,6,4,1],
#     [5,8,3,2,4,8,3],
#     [7,4,8,4,8,3,4]
# ]

# 다익스트라 - heapq를 써서, 이동거리가 짧은 경우부터
# 시간복잡도 ElogV -> 10000 * log125*125 이므로 다익스트라로 해야함
import heapq

dx = (1,-1,0,0)
dy = (0,0,1,-1)

INF = int(1e9)
dist = [[INF]*n for _ in range(n)]
  
def dijkstra():
    q = []
    dist[0][0] = cost[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))
    while q:
        distance, x, y = heapq.heappop(q)
        if dist[x][y] < distance:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < n):
                dc = distance + cost[nx][ny]
                if dc < dist[nx][ny]:
                    dist[nx][ny] = dc
                    heapq.heappush(q, (dc, nx, ny))

dijkstra()
print(dist[n-1][n-1])

