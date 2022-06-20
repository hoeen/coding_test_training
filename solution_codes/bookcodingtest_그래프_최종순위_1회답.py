# ~ 1:40
# t = int(input())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
rank = list(map(int, input().split()))

parent = list(range(n+1))

m = int(input())
change = []
for _ in range(m):
    change.append(tuple(map(int, input().split())))

for a, b in change:
    union_parent(parent, a, b)

print(parent)
# case: ?
def check():
    new_rank = [r for r in rank]
    for a, b in change:
        if parent[a] != parent[b]:
            print('IMPOSSIBLE')
            return

        apos = rank.index(a) 
        bpos = rank.index(b)
        order = 'asc'
        if apos < bpos:
            start, end = apos, bpos
        else:
            order = 'desc'
            start, end = bpos, apos

        if apos-bpos > 1: # 사이에 다른 팀 존재
            for c in rank[start+1:end]:
                if parent[c] != parent[a]:
                    print('?')
                    return
        
        print(apos,bpos,order)
        # 검사 통과한 경우 순위 변경
        napos, nbpos = new_rank.index(a), new_rank.index(b)
        if (order == 'asc' and napos < nbpos) or (order == 'desc' and napos > nbpos):
            new_rank[napos], new_rank[nbpos] = new_rank[nbpos], new_rank[napos]
    
    print(new_rank)
    return
        
check()


# case: impossible

# case: possible

