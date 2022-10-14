# 1시 간30분
# 14:45 ~ 15:00 15분
# 17:20 ~ 18:00 40분

def rotate():
    global A, robots, q
    # A 회전
    A = [A[-1]] + A[:-1]
    # 로봇 회전
    robots = [robots[-1]] + robots[:-1]
    # 로봇 내림
    if robots[n-1] > 0:
        # print('robot out')
        robots[n-1] = 0
        q.popleft()

def put_robot(rn):
    if A[0] > 0 and robots[0] == 0:
        robots[0] = rn
        A[0] -= 1
        q.append(rn)
        return True
    return False

def move_robot():
    global A
    # robot 올린 순서대로 번호 부여
    qr = deque(list(q))
    while qr:
        rn = qr.popleft()
        # rn 위치 찾고 조건에 맞게 이동
        ri = robots.index(rn)
        rnext = (ri+1) % (2*n)
        if A[rnext] > 0 and robots[rnext] == 0: # 한칸 전진
            robots[ri], robots[rnext] = robots[rnext], robots[ri]
            A[rnext] -= 1
    if robots[n-1] > 0:
        # print('robot out')
        robots[n-1] = 0
        q.popleft()


# import sys
# sys.stdin = open('input.txt', "r")
from collections import deque
# 컨베이어 벨트
n, k = map(int, input().split())
A = list(map(int, input().split()))
# A1, A2 ~ An
robots = [0]*(2*n)
step = 0
q = deque([])
rn = 1
while True:
    step += 1
    # print('step:', step)
    # print('q:', q)

    # 1이 올리는 위치, N 이 내리는 위치

    rotate()
    # print('rotate:')
    # print('conv:', A)
    # print('robots:', robots)

    move_robot()
    # print('move_robot:')
    # print('conv:', A)
    # print('robots:', robots)

    if put_robot(rn):
        rn += 1
        # print('put_robot:')
        # print('conv:', A)
        # print('robots:', robots)

    count = 0
    for c in A:
        if c == 0:
            count += 1
    if count >= k:
        print(step)
        break
