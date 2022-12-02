from itertools import permutations

n = int(input())

left_tall = [0] + list(map(int, input().split()))

for perm in permutations(range(1, n+1), n):
    for i in range(1, n+1):
        loc = perm.index(i) #0~n-1
        left_howmany = left_tall[i]
        taller_count = 0
        for l in perm[:loc]:
            if l > i:
                taller_count += 1
        if taller_count == left_howmany:
            


