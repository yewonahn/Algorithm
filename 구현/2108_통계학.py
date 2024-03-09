# 풀이 참조
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# 1. 산술 (반올림)
# round
print(round(sum(numbers) / n))

# 2. 중앙
numbers.sort()
print(numbers[n//2])

# 3. 최빈
# dict()
dic = dict()
# key : 값, value = 빈도수
for i in numbers:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 빈도수 중 최대값
mx = max(dic.values())
# 최빈값 저장
mx_lst = []

for key, value in dic.items():
    if value == mx:
        mx_lst.append(key)

if len(mx_lst) == 1:
    print(mx_lst[0])
else:
    print(sorted(mx_lst)[1])

# 4. 범위
# 이미 sort 되어있으므로 max, min 안써도됨
print(numbers[-1] - numbers[0])
