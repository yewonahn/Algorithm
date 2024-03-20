import sys
input = sys.stdin.readline

n = int(input())
storage = list(map(int, input().strip().split()))

# 최소 한 칸 이상 떨어진 창고 약탈

# 1. 접근법 파악
# 현재의 최적 해가 전체의 최적 해 보장 x -> 그리디 x

# 2. DP 조건 만족 여부
# 각 창고 storage[i] 에서 가능한 케이스 2가지
# storage[i+2] / storage[i+3]

# 각 케이스에서 다시 2가지 케이스로 쪼개서... -> 작은 문제로 쪼갬
# 동일 케이스 반복적 등장
# -> 최적 부분 구조 / 중복 되는 부분 문제 만족
# -> DP 로 시도

# storage[i] = max(storage[i+2], storage[i+3]) 만족

def check(i):
    if i == n-4:
        # n =  3 or 4칸인 경우 에도 storage[0] 포함 되도록
        if n == 3 or n == 4:
            return storage[i] + max(storage[n-2], storage[n-1])
        else:
            return max(storage[n-2], storage[n-1])
    elif i == n-3:
        # n = 3 or 4칸인 경우 에도 storage[0] 포함 되도록
        if n == 3 or n == 4:
            return storage[i] + storage[n - 1]
        else:
            return storage[n-1]
    else:
        return storage[i] + max(check(i+2), check(i+3))


result = max(check(0), check(1))

print(result)
