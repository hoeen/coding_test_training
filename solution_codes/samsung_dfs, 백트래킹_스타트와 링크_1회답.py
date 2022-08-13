# ~7:00
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

# n = 4
# s = [ 
# [0, 1, 2, 3],
# [4, 0, 5, 6],
# [7, 1, 0, 2],
# [3, 4, 5, 0],
# ]

def dfs(depth, idx):
    global min_diff
    # depth 가 n // 2일때, visited 아닌곳이 자동으로 상대편
    # 점수를 계산해서 최소값 갱신
    if depth == n // 2:
        print('reached. depth == ', n // 2)
        print('visited:', visited)
        score1, score2 = 0, 0
        for v in range(n):
            if visited[v]: 
                # v 이전까지의 visited를 찾아 s[i][j] 를 더함
                for j in range(v):
                    if visited[j]:
                        score1 += (s[j][v] + s[v][j])       
            else:
                for k in range(v):
                    if not visited[k]:
                        score2 += (s[k][v] + s[v][k])
        diff = abs(score1 - score2)
        if diff < min_diff:
            min_diff = diff
        return
        
    # dfs로 depth 증가시키면서 여러 경우로 재귀. combination 과 유사함
    for i in range(idx, n):
        print('not reached, depth = ', depth)
        print('visited = ', visited)
        visited[i] = True
        dfs(depth+1, i+1)
        visited[i] = False
        
min_diff = int(1e9)
visited = [False]*n

dfs(0, 0)

print(min_diff)





