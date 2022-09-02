# ~9:30 50분
n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]

# 드래곤 커브와 네 점이 만나는 사각형의 수를 구하자.
# x가 열, y가 행
dx = (0, -1, 0, 1)  # 0123 방향에 맞게
dy = (1, 0, -1, 0)
def dragon(y, x, d, g):
    dot_list = []
    navi = []
    # 0세대 선 긋기
    dot_list.append((y, x))
    dot_list.append((y + dy[d], x + dx[d]))
    navi.append(d) # 방향을 추가
    for i in range(1, g+1):
        # 끝점부터 방향 리스트 만들기
        for na in navi[::-1]:  # [d]
            # 시계 90도 회전
            na_90 = (na+1) % 4
            navi.append(na_90)
        # 처음 점부터 시작하여 만들어진 navi로 새로운 dot_list 생성
        dot_list = [(y, x)]
        nx, ny = x, y
        for na in navi:
            nx, ny = nx + dx[na], ny + dy[na]
            dot_list.append((ny, nx))

    return dot_list

# 드래곤 커브로 지나가는 모든점 set으로 중복없이 저장
dot_set = set()
for x, y, d, g in curves:
    dot_set.update(dragon(x,y,d,g))

# 4개점 겹치는 사각형 개수 세기
squares = 0
for sx in range(1, 101):
    for sy in range(1, 101):
        sq_set = {(sx-1, sy-1), (sx, sy-1), (sx-1, sy), (sx, sy)}
        if sq_set & dot_set == sq_set:
            squares += 1

print(squares)
             