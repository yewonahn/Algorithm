import sys
input = sys.stdin.readline

# 스위치 개수 (s <= 100)
s = int(input())
# 스위치 상태
# 1 켜 / 0 꺼
# 스위치 번호 0 부터 시작 (= 여기에서 인덱스 + 1)
state = list(map(int, input().strip().split()))
# 학생 수 (n <= 100)
n = int(input())
# 성별 / 스위치 번호
# 1 남 / 2 여
inf = [list(map(int, input().strip().split())) for _ in range(n)]

# 스위치 상태 인덱스
def change(i):
    global state
    if state[i] == 0:
        state[i] = 1
    else:
        state[i] = 0

for man in inf:
    # 남자
    if man[0] == 1:
        # 스위치 번호
        for i in range(man[1], s+1):
            if i % man[1] == 0:
                change(i-1)
    # 여자
    # 기준 숫자 = man[1]
    else:
        x = 0
        min, max = 0, 0
        # 스위치 번호
        while man[1] - (x+1) >= 1 and man[1] + x+1 <= s:
            x += 1
            # 스위치 상태 인덱스
            if state[man[1] - x - 1] != state[man[1] + x - 1]:
                x -= 1
                break
        for i in range(man[1] - x - 1, man[1] + x):
            change(i)

# 한 칸씩 비워서 출력
# 한 줄에 20개 까지 출력
for i in range(0, s):
    print(state[i], end=" ")
    # 인덱스 시작 0 이므로 i+1
    if i != 0 and (i+1) % 20 == 0:
        print()
