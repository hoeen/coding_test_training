# ~12:00 1시간 50분
def insert_queue():
    queue = deque([])
    sx, sy = n//2, n//2
    dx = (0, 1, 0, -1) #좌 하 우 상
    dy = (-1, 0, 1, 0)
    di = -1
    for i in range(1, n):
        di = (di + 1) % 4
        for _ in range(i):
            sx, sy = sx + dx[di], sy + dy[di]
            queue.append(board[sx][sy])
        di = (di + 1) % 4
        for _ in range(i):
            sx, sy = sx + dx[di], sy + dy[di]
            queue.append(board[sx][sy])
    # 마지막은 n-1개만큼 삽입
    di = (di + 1) % 4
    for _ in range(n-1):
        sx, sy = sx + dx[di], sy + dy[di]
        queue.append(board[sx][sy])
        
    return queue

def bliz(d, s):
    global queue
    # s 거리 1이면 3제곱, 2이면 5제곱, ..
    b_list = [] # 마법 적용 구슬 리스트
    sq = 1
    dist = 0
    for _ in range(s):
        sq += 2
        dist += 1
        # d 1 4 2 3 에 따라서 다른 값들을 집어넣는다.
        if d == 1:
            b_list.append((sq**2)-1-dist)
        elif d == 4:
            b_list.append((sq**2)-1-3*dist)
        elif d == 2:
            b_list.append((sq**2)-1-5*dist)
        else:
            b_list.append((sq**2)-1-7*dist)
    # b_list의 인덱스에 해당하는 구슬을 파괴
    # print(b_list)
    for idx in b_list:
        queue[idx-1] = 0
    
def push_zero(queue):
    new_q = deque([])
    while queue:
        qn = queue.popleft()
        if qn != 0:
            new_q.append(qn)
    return new_q

def explode(queue):
    global marbles
    exp = False
    new_q = deque([])
    if queue:
        q_init = queue.popleft()
    while queue:
        q_next = queue.popleft()
        if q_init != q_next:
            new_q.append(q_init)
            q_init = q_next
            continue
        else:
            temp = deque([])
            temp.append(q_init)
            while queue:
                q_more = queue.popleft()
                if q_more == q_next:
                    temp.append(q_next)
                    q_next = q_more
                    continue
                else:
                    temp.append(q_next)
                    q_init = q_more
                    break
        if len(temp) >= 4:
            exp = True
            marbles[temp[0]] += len(temp)
            continue # temp를 큐에 안 넣고 지나감
        else:
            while temp:
                t = temp.popleft()
                new_q.append(t)
        if not queue:
            new_q.append(q_init)
    return new_q, exp

def change(queue):
    new_q = deque([])
    if queue:
        q_init = queue.popleft()
    while queue:
        q_next = queue.popleft()
        if q_init != q_next:
            new_q.append(1)
            new_q.append(q_init)
            q_init = q_next
            continue
        else:
            temp = deque([])
            temp.append(q_init)
            while queue:
                q_more = queue.popleft()
                if q_more == q_next:
                    temp.append(q_next)
                    q_next = q_more
                    continue
                else:
                    temp.append(q_next)
                    q_init = q_more
                    break
            new_q.append(len(temp))
            new_q.append(temp[0])
        if not queue:
            new_q.append(1)
            new_q.append(q_init)
    return new_q

import sys
from collections import deque

input = sys.stdin.readline
# sys.stdin = open('input.txt', "r")

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
skill = [list(map(int, input().split())) for _ in range(m)]


# 먼저 queue 에 다 집어넣기
queue = insert_queue()

marbles = {
    1:0,
    2:0,
    3:0
}
# 스킬 1번 쓸때
for d, s in skill:
    # 블리자드
    bliz(d, s)

    # print(queue)

    # 빈칸 이동
    while True:
        queue = push_zero(queue)
        # print('push_zero:', queue)

        queue, exp = explode(queue)
        # print('explode:', queue)
        if exp is False:
            break

    queue = change(queue)


print(marbles[1] + 2*marbles[2] + 3*marbles[3])