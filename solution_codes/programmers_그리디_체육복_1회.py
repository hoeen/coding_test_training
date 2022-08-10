# ~4:30
def solution(n, lost, reserve):
    # lost에 없는 남은 체육복 학생들이 lost에 빌려준다.
    # lost랑 번호 차이가 1만 나야 한다.
    new = []
    # lost와 reserve에 같이 있는 경우,
    # 1 더하고 lost, reserve에서 같이 뺀다.
    overlap = []
    for l in lost:
        if l in reserve:
            print('중복', l)
            reserve.remove(l)
            overlap.append(l)
            print(reserve)

    lost = list(set(lost) - set(overlap))
    


    for l in lost:
        print('l', 'lost')
        print(l)
        print(lost)
        
        
        l1 = l - 1 # 입을수있는 사이즈
        l2 = l + 1
        if l1 in reserve:
            new.append(l)
            reserve.remove(l1)
            print('l1')
            print(l, l1)
            continue # 다음으로 넘어감
        if l2 in reserve:
            new.append(l)
            reserve.remove(l2)
            print('l2')
            print(l, l2)
            continue
    answer = n - (len(lost)-len(new))
    return answer

print(solution(5, [1,2], [2,3,5]))