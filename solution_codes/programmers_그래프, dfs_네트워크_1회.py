# ~12:30

# 서로소 집합 풀이
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
        
def solution(n, computers):
    parent = list(range(0,n)) #0 ~ n-1
    for x in range(n):
        for y in range(x):
            # print(x,y)
            if computers[x][y] == 1:
                union_parent(parent, x, y)
    print(parent[:])
    answer = len(set(parent[:]))
    return answer

print(solution(5, [[1,0,0,0,0],
                   [0,1,0,0,0],
                   [0,0,1,0,1],
                   [0,0,0,1,0],
                   [0,0,1,0,1]
                   ]))




