# 리스트 복사 참조
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# 산술
# 반올림
sum = 0
for a in numbers:
    sum += a
print(round(sum / n))

# 중앙
numbers.sort()
print(numbers[n//2])

# 최빈
cnt = []
# print("cnt : ", cnt)
m = numbers.copy()
while m:
    # count 하고 바로 pop
    cnt.append(m.count(m[0]))
    m.remove(m[0])
cnt.sort()
# print(cnt)
if len(cnt) == 1:
    print(cnt[0])
else:
    print(cnt[1])

# 범위
print(numbers[n-1] - numbers[0])
