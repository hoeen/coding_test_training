# ~7:40
n = int(input())
seq = list(map(int, input().split()))
seq.sort()

left = 0
right = n-1

min_sum = (int(1e13), int(1e13))
exited = False
while left < right:
    if seq[left] + seq[right] == 0:
        print(seq[left], seq[right])
        exited = True
        break
    elif seq[left] + seq[right] < 0:
        if abs(sum(min_sum)) > abs(seq[left] + seq[right]):
            min_sum = (seq[left], seq[right])
        left += 1
    else:
        if abs(sum(min_sum)) > abs(seq[left] + seq[right]):
            min_sum = (seq[left], seq[right])
        right -= 1

if not exited:
    print(min_sum[0], min_sum[1])

