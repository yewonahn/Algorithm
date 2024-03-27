# Counter, sorted 참조

from collections import Counter
import sys
input = sys.stdin.readline

name = list(input().strip())
alphb = Counter(name)

check = False
charac = ''
# 홀수인 알파벳 개수
cnt = 0
for key in alphb:
    if alphb[key] % 2 == 1:
        cnt += 1
        charac = key
        check = True
        # 1. 홀수 개인 알파벳이 두 개 이상 -> 안됨
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            # 종료
            exit()

for key in sorted(alphb.keys()):
    if key != charac:
        print(key * (alphb[key] // 2), end='')
    # 2. 홀수 개인 알파벳 한 개 -> 한 개만 가운데 출력
    else:
        print(key * (alphb[key] // 2), end='')
if check:
    print(charac, end='')
for key in sorted(alphb.keys(), reverse=True):
    if key != charac:
        print(key * (alphb[key] // 2), end='')
    # 2. 홀수 개인 알파벳 한 개 -> 한 개만 가운데 출력
    else:
        print(key * (alphb[key] // 2), end='')
