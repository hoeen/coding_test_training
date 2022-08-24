# 1시간
# ~11:00
gears = [[]] + [list(map(int, input())) for _ in range(4)]

n = int(input())
rot = [list(map(int, input().split())) for _ in range(n)]

# 회전 리스트 반환 함수
def rotate(num, di):
    global gears
    gear = gears[num][:]
    if di == 1: # 시계
        new_gear = [gear[-1]] + gear[:-1]
    else: # 반시계
        new_gear = gear[1:] +[gear[0]]
    gears[num] = new_gear
    return

# 같이 회전할 대상 정하는 함수
def which_to_rotate(num, di):
    # 묶인 부분 - 1번 2, 2번 6 2, 3번 6 2, 4번 6
    rot_gears = [[num, di]]
    leftgear = gears[num][6]
    rightgear = gears[num][2]

    # 왼쪽 체크
    check = num - 1 
    rotate = di
    while check > 0:
        if gears[check][2] != leftgear:
            rotate *= -1
            rot_gears.append([check, rotate])
        else:
            break
        leftgear = gears[check][6]
        check -= 1
    
    # 오른쪽 체크
    check = num + 1 
    rotate = di
    while check < 5:
        if gears[check][6] != rightgear:
            rotate *= -1
            rot_gears.append([check, rotate])
        else:
            break
        rightgear = gears[check][2]
        check += 1
    return rot_gears # 회전할 기어 반환


# 먼저 회전 대상 정하고, 맞붙은 곳 확인, 극이 만약 다르면 반대로 회전. 끝.
for num, di in rot:
    rotate_cand = which_to_rotate(num, di)
    for gn, gd in rotate_cand:
        rotate(gn, gd)
    
# 점수 계산    
answer = 0
points = [None,1,2,4,8]
for i in range(1, 5): #1~4
    if gears[i][0] == 1:
        answer += points[i]

print(answer)
