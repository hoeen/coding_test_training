# ~ 12:15   # ~ 12:40분 완료. 총 1시간 
n, m, k = map(int, input().split())
plan = [list(map(int, input().split())) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]

# n, m, k = 1, 1, 1
# plan
# trees


# n = 4
# 나무 위치에 심기
tree_land = [[[] for _ in range(n)] for _ in range(n)]
for x, y, age in trees:
    tree_land[x-1][y-1].append(age)
# 처음 비료 구현
comp_land = [[5]*n for _ in range(n)]

# 봄
# 나무가 나이만큼 양분 먹고 1 증가
# 나이 어린 나무부터 양분 먹음
# 양분 못먹으면 즉시 죽음
def spring():
    dead_trees = []
    for x in range(n):
        for y in range(n):
            # 나무가 있을 경우 어린 순으로 나이 sort
            if tree_land[x][y]:
                tree_land[x][y].sort()
                new_trees = []
                for age in tree_land[x][y]:
                    if age <= comp_land[x][y]:
                        comp_land[x][y] -= age
                        new_trees.append(age+1)
                    else: # 죽은 나무 명단 - (x, y, age)추가
                        dead_trees.append((x, y, age))
                tree_land[x][y] = new_trees
    return dead_trees

def summer(dead_trees):
    # 여름 - 봄에 죽은 나무가 양분으로 변함.
    for x, y, age in dead_trees:
        comp_land[x][y] += age // 2

# 가을 - 나무 번식, 5의 배수만 번식
# 인접한 8개칸에 나이가 1인 나무 생김
def autumn():
    son_tree_land = [t[:] for t in tree_land]
    # 8방
    dx = (-1, -1, -1, 0, 0, 1 ,1 ,1)
    dy = (-1, 0, 1, -1, 1, -1, 0 ,1)
    for x in range(n):
        for y in range(n):
            if tree_land[x][y]: # 나무 있을경우
                for age in tree_land[x][y]:
                    if age % 5 == 0:
                        # 주변에 나무심기
                        for i in range(8):
                            nx, ny = x + dx[i], y + dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                son_tree_land[nx][ny].append(1) # 새나무 추가
                         
    return son_tree_land

def winter():
    for x in range(n):
        for y in range(n):
            comp_land[x][y] += plan[x][y]

          
for i in range(k):
    # print('year:', i)
    dead_trees = spring()
    
    # print('spring - trees')
    # for t in tree_land:
    #     print(t)
    # print('dead trees')
    # print(dead_trees)

    summer(dead_trees)
    son_tree_land = autumn()
    tree_land = [t[:] for t in son_tree_land]
    winter()
    # print('check')
    # print('comp')
    # for c in comp_land:
        # print(c)
    # print('trees')
    # for t in tree_land:
        # print(t)
    
    # print('survived:', survived)

# 살아남은 나무 수 출력
survived = 0
for x in range(n):
    for y in range(n):
        survived += len(tree_land[x][y])

print(survived)

