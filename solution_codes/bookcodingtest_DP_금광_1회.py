# 첫번째 열 어느 행이든 출발 가능
# 출발 이후엔 열 개수 M 만큼 오른쪽위, 오른쪽, 오른쪽아래 세방향으로만 이동가능
# ~12:00
# dp
# 점화식 - f(k) = f(k-1) + m
n, m = map(int, input().split())

input_list = list(map(int, input().split()))
board = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        num = input_list.pop(0)
        board[x][y] = num

dx = (-1,0,1)
cand = []
def dfs(x, y, total):
    total += board[x][y]
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if ny == m:
            cand.append(total)
            return
        elif (0 <= nx < n) and (0 <= ny < m):
            dfs(nx, ny, total)
        else:
            return None

import time

t0 = time.time()
for i in range(n):
    dfs(i, 0, 0)

print(cand)
print(max(cand))
print(time.time() - t0)

    




def dp_tab():
    tab = [[0]*m for _ in range(n)]
    for i in range(n):
        tab[i][0] = board[i][0]
    
    for y in range(1, m):
        for x in range(0, n):
            fm = []
            for i in range(3):
                nx = x + dx[i]
                if (0 <= nx < n):
                    fm.append(tab[nx][y-1])
            print(x, y, fm)
            tab[x][y] = board[x][y] + max(fm)
    return tab

t0 = time.time()
ans_table = dp_tab()

# print('ans_table')
# for ans in ans_table:
#     print(ans)


ans_cand = []
for i in range(n):
    ans_cand.append(ans_table[i][m-1])

print(max(ans_cand))
print(time.time() - t0)
        


    
# [ 1 3 1 5
#   2 2 4 1
#   5 0 2 3
#   0 6 1 2 ]