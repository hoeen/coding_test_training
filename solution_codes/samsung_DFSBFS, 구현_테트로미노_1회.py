# ~5:10 / 5:40 / 6:10
'''
테트로미노 하나를 적절히 놓아서 
테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
'''
# N열 M행
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# board = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))

# max testcase
import time
t0 = time.time()
board = [[1,2]*250 for _ in range(4)]


# board = [ 
#     [1,2,3,4,5],
#     [5,4,3,2,1],
#     [2,3,4,5,6],
#     [6,5,4,3,2],
#     [1,2,1,2,1]
# ]

# board = [ 
#     [1,2,1,2,1,2,1,2,1,2],
#     [2,1,2,1,2,1,2,1,2,1],
#     [1,2,1,2,1,2,1,2,1,2],
#     [2,1,2,1,2,1,2,1,2,1]
# ]

# board = [ 
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5],
#     [1,2,3,4,5]
# ]

# board = [ 
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# # 테트로미노 5가지 - 4 dfs + 1 bfs

dx = (-1,0,1,0)
dy = (0,-1,0,1)

'''
 1,2,3,4 를 4번 뽑는경우 리스트해서 
각각의 경우에서 visited 처리하고 범위 안벗어나면 더한다.
더한값을 cand 에 append하여 최댓값을 뽑아낸다.
'''

total_case = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            total_case.append([i,j,k])




def tet(x,y):
    num_list = [[board[x][y]] for _ in range(len(total_case))]
    for p in range(len(total_case)): #p = [0,1,2]
        visited = [[False]*m for _ in range(n)]
        visited[x][y] = True
        nx, ny = x, y
        for dir in total_case[p]: # dir = 0 / 1 / 2 / 3
            nx += dx[dir]
            ny += dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            else:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    num_list[p].append(board[nx][ny])
                else:
                    break
        
    return max([sum(i) for i in num_list if len(i) == 4])




def oh_tet(x,y):
    oh_list = []
    oh = [] # 귀퉁이 모음
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        else:
            oh.append(board[nx][ny]) 
    if len(oh) != 4:
        oh_list.append(oh)
    else:
        for i in range(4):
            ohr = [j for j in oh]
            ohr.pop(i)
            oh_list.append(ohr)
    return max([sum(o) for o in oh_list]) + board[x][y]



ans_list = []
for x in range(n):
    for y in range(m):
        ans_list.append(max(tet(x,y),oh_tet(x,y)))
print(max(ans_list))


print(time.time() - t0)

# visited = []
# tetsum = []
# count = 0
# def dfs(x,y):
#     link = []  
#     cand = []
#     visited = [[0]*n for _ in range(n)]
#     stack = []
#     # 방문처리
#     visited[x][y] = 1 # 길이로 표시
#     stack.append((x,y))

#     while stack:
#         xs, ys = stack.pop() # 맨 끝에서 뺀다
        
#         for i in range(3):
#             nx = xs + dx[i]
#             ny = ys + dy[i]
#             if not visited[nx][ny]:
#                 visited[nx][ny] = visited[xs][ys] + 1
#                 stack.append((nx,ny))
#                 # 어디서 왔는지 링크 정보 저장
#                 link.append(((xs,ys),(nx,ny)))
                
#                 # 끝까지 도달했을때
#                 if visited[nx][ny] == 4:
#                     # 링크따라서 모두 더하고 그 값을 cand 에 append
#                     sum_value = board[nx][ny]
#                     while (nx,ny) != (x,y):
#                         for l in link:
#                             if l[1] == (nx,ny):
#                                 bx, by = l[0]
#                                 sum_value += board[bx][by]
#                                 nx,ny = bx,by
#                     sum_value += board[x][y]
#                     cand.append(sum_value)
                                
                        
                            















    # global count
    # tet = board[x][y] 
    # print(x,y)
    # print(tet)

    # visited.append((x,y)) 
    # for i in range(3):
    #     nx = x+dx[i]
    #     ny = y+dy[i]
    #     if nx >= 0 and nx < n and ny >= 0 and ny < n:
    #         if (nx,ny) not in visited:
    #             if count == 0:
    #                 count += 1
    #                 tetsum.append(tet + dfs(nx, ny, visited))
    #                 print(tetsum)
    #                 return 
    #             elif count <= 3:
    #                 count += 1
    #                 print(tet)
    #                 return tet + dfs(nx, ny, visited)
                    
    #             elif count == 3:
    #                 print(tet)
    #                 return tet 
    #     else:
    #         return 
           

    
    
