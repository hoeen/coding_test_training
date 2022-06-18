# ~1:15
# 최대 모험가 그룹
n = int(input())
# ppl_list = [int(i) for i in input().split()]
ppl_list = [5, 2, 1, 1, 1, 1, 1, 1]

# 제일 구성 많이 하려면, 3인 사람 부터 2를 최대한 껴준다.
# 최대한 많은 사람에게 적은 사람을 붙여주고, 그다음 남은걸로 처리
# 일단 정렬
sort_list = sorted(ppl_list, reverse=True)
print(sort_list)
# 최대랑 그룹을 결정지어서 빼고, count를 한다
# [3,2,2,2,1]

# 첫번째 확인
count = 0
pick = 0
while True:
    pick = sort_list[0]
    if len(sort_list) > pick: # 뽑아도 남는경우
        # pick 수 - 1 만큼 슬라이싱
        sort_list = sort_list[pick:]
        count += 1
    else:  # 딱 맞거나 덜 남는경우
        count += 1
        break


print(count)

    

 