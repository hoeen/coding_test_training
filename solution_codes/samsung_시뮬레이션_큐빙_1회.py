from copy import deepcopy

# 3시간 가까이 소요
t = int(input())
planes = ['U', 'D', 'F', 'B', 'L', 'R']
colors = list('wyrogb')

pl_dic = {
        'U': tuple('BRFL'),
        'D': tuple('BLFR'),
        'L': tuple('UFDB'),
        'R': tuple('UBDF'),
        'B': tuple('ULDR'),
        'F': tuple('URDL')
    }

def matrix_rotate(mat, clock):
    new_mat = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if clock:
                new_mat[j][2-i] = mat[i][j]
            else:
                new_mat[2-j][i] = mat[i][j]
    return new_mat

def change_cube(p0, clock, temp_pl):
    global init
    # 위쪽부터 시계 방향으로 p1, p2, p3, p4
    p1, p2, p3, p4 = pl_dic[p0]
    if clock:
        init[p1] = [temp_pl[p4][0]] + temp_pl[p1][1:]
        init[p2] = [temp_pl[p1][0]] + temp_pl[p2][1:]
        init[p3] = [temp_pl[p2][0]] + temp_pl[p3][1:]
        init[p4] = [temp_pl[p3][0]] + temp_pl[p4][1:]
    else:
        init[p1] = [temp_pl[p2][0]] + temp_pl[p1][1:]
        init[p2] = [temp_pl[p3][0]] + temp_pl[p2][1:]
        init[p3] = [temp_pl[p4][0]] + temp_pl[p3][1:]
        init[p4] = [temp_pl[p1][0]] + temp_pl[p4][1:]
    return


# 모든 면은 U를 위로 기준, U와 D는 B를 위로 기준.
def rotate(plane, clock): # U, True - clock, False - counterclock
    temp_pl = deepcopy(init)
    init[plane] = matrix_rotate(init[plane], clock) # 90도 시계방향 회전
    # breakpoint()
    
    if plane == 'U':
        # 회전 안시키고 그대로 cube 실행
        change_cube(plane, clock, temp_pl)
    elif plane == 'D':
        # 180도 회전
        for pl in pl_dic[plane]:
            r1 = matrix_rotate(init[pl], True)
            temp_pl[pl] = matrix_rotate(r1, True)
        change_cube(plane, clock, temp_pl)
        # 다시 180도 회전
        for pl in pl_dic[plane]:
            r1 = matrix_rotate(init[pl], True)
            r2 = matrix_rotate(r1, True)
            init[pl] = r2
    elif plane == 'L':
        # U F 90도, B D -90도
        for pl in pl_dic[plane]:
            if pl in ['U', 'F']:
                temp_pl[pl] = matrix_rotate(init[pl], True)
            else:
                temp_pl[pl] = matrix_rotate(init[pl], False)
        change_cube(plane, clock, temp_pl)
        # 원래대로
        for pl in pl_dic[plane]:
            if pl in ['U', 'F']:
                init[pl] = matrix_rotate(init[pl], False)
            else:
                init[pl] = matrix_rotate(init[pl], True)
    elif plane == 'R':
        for pl in pl_dic[plane]:
            if pl in ['U', 'F']:
                temp_pl[pl] = matrix_rotate(init[pl], False)
            else:
                temp_pl[pl] = matrix_rotate(init[pl], True)
        change_cube(plane, clock, temp_pl)
        # 원래대로
        for pl in pl_dic[plane]:
            if pl in ['U', 'F']:
                init[pl] = matrix_rotate(init[pl], True)
            else:
                init[pl] = matrix_rotate(init[pl], False)
    elif plane == 'F':
        # U D 180도, L -90도, R 90도
        for pl in pl_dic[plane]:
            if pl == 'L':
                temp_pl[pl] = matrix_rotate(init[pl], False)
            elif pl == 'R':
                temp_pl[pl] = matrix_rotate(init[pl], True)
            else:
                r1 = matrix_rotate(init[pl], True)
                temp_pl[pl] = matrix_rotate(r1, True)
        change_cube(plane, clock, temp_pl)
        # 원래대로
        for pl in pl_dic[plane]:
            if pl == 'L':
                init[pl] = matrix_rotate(init[pl], True)
            elif pl == 'R':
                init[pl] = matrix_rotate(init[pl], False)
            else:
                r1 = matrix_rotate(init[pl], True)
                init[pl] = matrix_rotate(r1, True)
    elif plane == 'B':
        for pl in pl_dic[plane]:
            if pl == 'L':
                temp_pl[pl] = matrix_rotate(init[pl], True)
            elif pl == 'R':
                temp_pl[pl] = matrix_rotate(init[pl], False)
        change_cube(plane, clock, temp_pl)
        for pl in pl_dic[plane]:
            if pl == 'L':
                init[pl] = matrix_rotate(init[pl], False)
            elif pl == 'R':
                init[pl] = matrix_rotate(init[pl], True)

    return

for _ in range(t):
    # 각 면 상태 풀린채로 초기화
    init = dict()
    for p in range(6):
        init[planes[p]] = [[colors[p]]*3 for _ in range(3)]

    n = int(input())
    coms = [(com[0], [True if com[1] == '+' else False][0]) for com in input().split()]
   
    for plane, cw in coms:
        rotate(plane, cw)

    # print result
    for row in init['U']:
        print(''.join(row))

