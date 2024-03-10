# 풀이 참조

import sys
input = sys.stdin.readline

n = input().strip()
cnt = [0] * 9

for i in n:
    # int('\n') : ValueError -> strip()
    num = int(i)
    if num == 9:
        num = 6
    cnt[num] += 1

# round 사사오입
cnt[6] = (cnt[6] + 1) // 2

print(max(cnt))
