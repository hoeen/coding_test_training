#~4:15
# 알파벳을 오름차순 정렬해서 출력 + 모든 숫자 더한값을 이어서 출력
first = list(input())
num = list('0123456789')

# 알파벳 정렬
first_sort = sorted(first)
num_idx = list()
char = list()
sum = 0
for i in range(len(first_sort)):
    if first_sort[i] in num:
        sum += int(first_sort[i])
        
    else:
        char.append(first_sort[i])

char.append(str(sum))
last = ''.join(char)

print(last)