board = [list(input()) for _ in range(5)]

# 7명 결성. 4명은 무조건 S로 포함
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
all_group = list() # {(x, y), (x1, y1)} 으로 구성된 리스트
dup_count = 0
# 모든 경우로 재귀 -> 연결된 경우, S 4개인경우를 리턴 - 백트래킹
def dfs(ppls: list, group: list, visited: list):
    global dup_count
    if ppls.count('Y') >= 4:
        return
    # exit
    if len(ppls) == 7:
        # S 4이상 - all_group에 있는지 보고 없으면 추가하기
        if ppls.count('S') >= 4:
            if set(group) not in all_group:
                all_group.append(set(group))   
            else:
                # print(group)
                dup_count += 1     
        return
    else:  
        for gx, gy in group:
            for i in range(4):
                nx, ny = gx + dx[i], gy + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        group.append((nx, ny))
                        ppls.append(board[nx][ny])
                        # 재귀 
                        dfs(ppls, group, visited)
                        visited[nx][ny] = False
                        group.pop(-1)
                        ppls.pop(-1)
                        
for x in range(5):
    for y in range(5):
        if board[x][y] == 'S':
            visited = [[False]*5 for _ in range(5)]
            visited[x][y] = True
            dfs(list(board[x][y]), [(x, y)], visited)

print(len(all_group))
print('duplicated:', dup_count)

# for g in all_group:
#     print('===========')
#     bb = [[False]*5 for _ in range(5)]
#     for gx, gy in g:
#         bb[gx][gy] = True
#     for b in bb:
#         print(b)

# print(all_group)


# print(len(all_group))
