n = int(input())

students = []
for _ in range(n):
    name, kuk, young, su = input().split()
    students.append([name, int(kuk), int(young), int(su)])
    
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])