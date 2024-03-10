import sys
input = sys.stdin.readline

# 하나씩 리스트에 저장
n = list(str(input().strip()))
for i in range(len(n)):
    n[i] = int(n[i])

# 최대 중복 개수 저장
# 6, 9 개수
max = round((n.count(6) + n.count(9)) // 2)

# 나머지 중복 숫자
for i in n:
    if i != 6 and i != 9:
        if n.count(i) > max:
            max = n.count(i)

print(max)
