# 한 장 남을떄까지 반복
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card = deque(i+1 for i in range(n))
#print(card)
# 버리는 카드 저장
trash = []

# 처음 주어진 카드가 n=1 인 상황 고려해야됨
while len(card) != 1:
    # 제일 위에꺼 버림
    trash.append(card.popleft())
    # 그 다음 위에 있는거 제일 밑으로 이동
    card.append(card.popleft())

if len(card) == 1:
    # trash 출력
    for i in range(len(trash)):
        print(trash[i], end=' ')

    # 마지막 남아있는 카드 번호 출력
    print(*card)
