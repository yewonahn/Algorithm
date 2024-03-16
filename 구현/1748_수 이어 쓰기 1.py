import sys
input = sys.stdin.readline

n = int(input())
# 1. 입력 받은 수가 몇 자릿 수 인지
length = len(list(str(n)))
result = 0

# 2. 자릿수 별로 확인
for i in range(0, length):
    # 2-1. max 자릿수 일 때
    if i == length - 1:
        # 3. (각 자릿수 마다, 자릿수 * 개수) 의 합
        # 3-1. max 자릿수 개수 구하기
        num = n - (10 ** (length - 1)) + 1
        # 3-2. i + 1 : 자릿수 길이
        result += num * (i + 1)
    # 2-2. max 자릿수 전 일 때
    else:
        # 3.
        # 자릿수 마다 개수 9 / 90 / 900 / 9000 ...
        # i + 1: 자릿수 길이 1 / 2 / 3 ...
        result += 9 * (10 ** i) * (i + 1)

print(result)
