# 링크 : https://2hs-rti.tistory.com/entry/백준-17852번-주사위-윷놀이-파이썬

move = list(map(int, input().split()))
horse = [[0, 0] for _ in range(4)]
road = [[i for i in range(0, 41, 2)],
        [i for i in range(0, 11, 2)]+[13, 16, 19],
        [i for i in range(0, 25, 2)],
        [i for i in range(0, 31, 2)]+[28, 27, 26],
        [25, 30, 35, 40]
        ]

def back_tracking(x, result, horse):
    global answer
    if x == 10:
        answer = max(answer, result)
        return
    for k in range(4):
        if horse[k][1] == -1: # 도착한 경우
            continue
        new_horse = [h[:] for h in horse]
        new_horse[k][1] += move[x]
        change_road(k, new_horse)
        # 도착 미도착 설정
        if new_horse[k][1] >= len(road[new_horse[k][0]]):
            new_horse[k][1] = -1
            back_tracking(x+1, result, new_horse)
        else:
            # 말이 있는지 없는지
            if [new_horse[k][0], new_horse[k][1]] in horse:
                continue
            back_tracking(x+1, result + road[new_horse[k][0]][new_horse[k][1]], new_horse)

def change_road(k, horse):
    if horse[k][0] == 0:
        if horse[k][1] == 5:
            horse[k][0] = 1
        elif horse[k][1] == 10:
            horse[k][0] = 2
        elif horse[k][1] == 15:
            horse[k][0] = 3
        elif horse[k][1] == len(road[horse[k][0]]) - 1:
            horse[k][0] = 4
            horse[k][1] = len(road[horse[k][0]]) - 1
    elif horse[k][0] != 4:
        if horse[k][1] >= len(road[horse[k][0]]):
            horse[k][1] = horse[k][1] - len(road[horse[k][0]])
            horse[k][0] = 4





answer = 0
back_tracking(0, 0, horse)
print(answer)
