kp, sp, n = input().split()
kc, kr = list(kp)
sc, sr = list(sp)
n = int(n)

for i in range(ord('A'), ord('H')+1):
    if ord(kc) == i:
        kca = ord(kc)-ord('A')
    if ord(sc) == i:
        sca = ord(sc)-ord('A')

kc, sc = kca, sca
kr = int(kr) - 1
sr = int(sr) - 1

coms = [input() for _ in range(n)]

arrow = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = (0, 0, -1, 1, 1, 1, -1, -1)
dy = (1, -1, 0, 0, 1, -1, 1, -1)

for c in coms:
    for i, di in enumerate(arrow):
        if c == di:
            nx = kr + dx[i]
            ny = kc + dy[i]
            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                break
            elif (nx, ny) == (sr, sc):
                sx = sr + dx[i]
                sy = sc + dy[i]
                if sx < 0 or sx >= 8 or sy < 0 or sy >= 8:
                    break
                sr, sc = sx, sy
            kr, kc = nx, ny
            break
# col + row
# king
print(chr(ord('A') + kc) + str(kr+1))

# stone
print(chr(ord('A') + sc) + str(sr+1))