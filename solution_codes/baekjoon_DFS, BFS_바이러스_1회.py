# ~11:10
n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(m)]

# bfs
# 1번 먼저 연결 확인
def bfs():
    infected = 0
    q = []
    visited = [False]*(n+1)
    visited[1] = True # 방문처리
    q.append(1)
    while q:
        num = q.pop(0)
        for g in graph:
            if num in g:
                b = list(set(g)-set([num]))[0]
                if not visited[b]:
                    q.append(b)
                    visited[b] = True
                    infected += 1
        # print('num:', num)
        # print('q:', q)
        # print('visited:', visited)
    return infected
print(bfs())