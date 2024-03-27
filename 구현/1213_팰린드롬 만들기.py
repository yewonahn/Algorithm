# [풀이 참조]
# Counter, sorted, 리스트.items(), 리스트 역순 접근 참조

from collections import Counter
import sys
input = sys.stdin.readline

name = list(input().strip())
# Counter : 각 원소가 몇 번씩 나오는지 저장된 딕셔너리 객체 반환
alphb = Counter(name)
# 홀수인 알파벳 개수
cnt = 0
mid = ''
result = ''

for k, v in list(alphb.items()):
    if v % 2 == 1:
        cnt += 1
        mid = k
        # 1. 홀수 개인 알파벳이 두 개 이상 -> 안됨
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

# sorted(alphb.items()) -> list 반환
# sorted(alphb.items()) 결과 리스트 [key, value] 가 저장되어 있음
print(alphb.items())
for k, v in sorted(alphb.items()):
    result += (k * (v // 2))

# result[::-1] : 리스트 역순 접근
print(result + mid + result[::-1])
