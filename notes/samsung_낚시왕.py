# 11:55~ 12:34 40분   + 30분 ~14:40
def catch(y):
    global bucket
    for r, c, s, d, z in sharks:
        if c == y:
            bucket += z
            sharks.remove([r,c,s,d,z])
            return
    return

def move():
    global sharks
    moved_sharks = []
    for r, c, s, d, z in sharks:
        # 상어가 속도 ,방향으로 이동. 벽 만나면 반대편
        length = s
        while length:
            nr, nc = r + dx[d-1], c + dy[d-1]
            if nr < 1 or nr > R or nc < 1 or nc > C:
                if d in (1,3):
                    d += 1
                else:
                    d -= 1
                nr, nc = r + dx[d-1], c + dy[d-1] # 반대 방향 전진
            r, c = nr, nc
            length -= 1
        moved_sharks.append([r, c, s, d, z])
    sharks = [s[:] for s in moved_sharks]

def eat():
    global sharks
    # r, c, 크기는 역순으로 정렬해서 같은 위치에 크기가 작은게 다음번이면 다음번 삭제
    sort_sharks = sorted(sharks, key = lambda x: (x[0],x[1],-x[4]))


    surv_sharks = [sort_sharks[0][:]]
    r0, c0 = sort_sharks[0][:2]
    for i in range(1, len(sharks)):
        r, c, z = sort_sharks[i][0], sort_sharks[i][1], sort_sharks[i][4]
        # nr, nc, nz = sort_sharks[i+1][0], sort_sharks[i+1][1], sort_sharks[i+1][4]
        if (r, c) == (r0, c0):
            continue
        else:
            surv_sharks.append(sort_sharks[i])
            r0, c0 = sort_sharks[i][:2]
    sharks = [s[:] for s in surv_sharks]
    return




dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
# r,c 위치 , s 속력, d 이동방향 (상 하 우 좌 ), z 크기


if M == 0:
    print(0)

else:

    fy = 0
    bucket = 0
    while fy < C:
        sharks.sort(key=lambda x: (x[1], x[0]))  # y, x 순으로 정리
        fy += 1

        # 가까운 상어를 잡는다.
        catch(fy)
        # 상어가 이동한다.
        move()
        # 상어가 잡아먹는다
        if sharks:
            eat()

    # print('잡은크기들')
    print(bucket)