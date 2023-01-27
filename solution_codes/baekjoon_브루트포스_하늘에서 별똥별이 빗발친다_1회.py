n, m, l, k = map(int, input().split())
star_loc = [list(map(int, input().split())) for _ in range(k)]

'''
1. bf - 하나씩 이동하면서 몇개튕겨내는지 계산
2. 좌표 정렬 - x최소, 
'''

max_stars = 0

xgrid = []
ygrid = []
for x, y in star_loc:
    xgrid.append(x)
    ygrid.append(y)
xgrid = list(set(xgrid))
ygrid = list(set(ygrid))
xgrid.sort()
ygrid.sort()

xarea = [-l, -l, l, l]
yarea = [l, -l, l, -l]

for x in xgrid:
    for y in ygrid:
        for i in range(4):
            stars = 0
            xm, ym = x + xarea[i], y + yarea[i]
            for sx, sy in star_loc:
                if x <= sx <= xm and y <= sy <= ym:
                    stars += 1
            if max_stars < stars:
                max_stars = stars

print(k-max_stars)


        


