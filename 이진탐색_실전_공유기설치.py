## ~2:30
n, c = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

# 최소, 최대 간격 설정
min_gap = 1
max_gap = array[-1] - array[0] 

# 최적의 인접간격 
result = 0

while min_gap <= max_gap:
    mid = (min_gap + max_gap) // 2 # 중간점을 간격으로 설정
    count = 1
    now = array[0]
    # 공유기 설치
    for i in range(1, len(array)):
        if array[i] - now >= mid:
            now = array[i] 
            count += 1
    if c <= count:  # 공유기가 확보된 양보다 더 설치된 경우: 간격 줄여서
        result = mid
        min_gap = mid+1  # 최소간격을 mid+1로 잡고 다시 실행
    else:       # 공유기 양만큼 설치가 불가능한 경우
        max_gap = mid-1 # 최대간격을 mid-1로 줄이고 다시 실행

print(result)