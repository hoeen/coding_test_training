# 12:05 시작  1시간 목표
import pdb, time

board = {
'0r':[2, 4, 6, 8, 10],
'10b':[13, 16, 19, 25],
'10r':[12, 14, 16, 18, 20],
'20b':[22, 24, 25],
'20r':[22, 24, 26, 28, 30],
'30b':[28, 27, 26, 25],
'30r':[32, 34, 36, 38, 40, 100],
'25r':[30, 35, 40, 100] # 100 : 도착
}

def move(pos_list, which, num):
    route, dist = pos_list[which]

    if route == False:
        route = '0r'

    dist += num

    if dist < len(board[route]) - 1:  # route 그대로, dist 그대로
        pass
    elif dist == len(board[route]) - 1:  # 딱 루트 끝점이면
        if board[route][dist] == 100:  # 도착
            route, dist = None, 100  # 점수 추가 없이 끝
        elif board[route][dist] != 25:  # '25r'
            # 다음 루트를 b로 전환, dist 는 -1
            route = str(board[route][dist]) + 'b'
            dist = -1
        else:  # 25가 끝점인 경우
            route = '25r'
            dist = -1
    elif dist > len(board[route]) - 1:  # 루트를 지나갔으면
        dist = dist - len(board[route])
        route = str(board[route][-1]) + 'r'
        if route == '100r':  # 도착점 도달했으면
            route, dist = None, 100

    return route, dist


def dfs(dice, pos_list, score): # dice : 주사위 숫자 리스트,
    global max_score
    # time.sleep(1)
    # if score == 214:
    #     print('214', dice, pos_list, score)
    # if score == 278:
    #     print('278', dice, pos_list, score)
    # exit
    if not dice: # 숫자 없으면 - 지금까지의 score를 최댓값과 비교해서 갱신
        if max_score < score:
            max_score = score
        print('renew - pos_list:', pos_list)
        print('renew score, max_score:', score, max_score)
        return
    #
    print('=' * 30)
    print('dice left:', dice)
    print('pos_list:', pos_list)
    print('score:', score)
    pdb.set_trace()

    for h in range(4):

        if pos_list[h][0] is None: # 선택했는데 도착한 말이면 - 같은 dice로 다음말 진행
            continue

        else: # 도착하지 않은 말이면
            print(f'h: {h}, score: {score}')

            # 주사위 숫자 확인
            num = dice[0]
            # h 에 해당하는 말을 나온 숫자만큼 옮기기.
            route, dist = move(pos_list, h, num)

            new_pos_list = [p[:] for p in pos_list]


            if (route, dist) == (None, 100):
                new_pos_list[h] = [route, dist]
                dfs(dice[1:][:], new_pos_list, score)
            else:
                # 말이 겹치게 이동할 수 없다 - 겹치는 경우이면 다시 되돌리기. 도착 칸이면 고를 수 있다.
                if [route, dist] in pos_list:
                    continue


                # 점수 추가
                if dist == -1:
                    new_score = score + int(route[:-1])
                else:
                    new_score = score + board[route][dist]

                # 다음 dice 번호로 재귀
                new_pos_list[h] = [route, dist]
                dfs(dice[1:][:], new_pos_list, new_score)






# dice = list(map(int, input().split()))
# dice = [5,1,2,3,4,5,5,3,2,4]
dice = [2, 2, 2, 2, 3, 2, 2, 2, 2, 2]
# dice = [1,2,3,4,1,2,3,4,1,2]
# dice = [1,2,3,4,3]
# 놀이판 구현
board = {
'0r':[2, 4, 6, 8, 10],
'10b':[13, 16, 19, 25],
'10r':[12, 14, 16, 18, 20],
'20b':[22, 24, 25],
'20r':[22, 24, 26, 28, 30],
'30b':[28, 27, 26, 25],
'30r':[32, 34, 36, 38, 40, 100],
'25r':[30, 35, 40, 100] # 100 : 도착
}

max_score = 0
# 첫 시작은 무조건 첫 번호로  말 하나 위치
# num = dice.pop(0)
# score = board['0r'][num-1]
# max_score += score
pos_list = [[False, -1] for _ in range(4)]

dfs(dice, pos_list, 0)

print('max_score:', max_score)





