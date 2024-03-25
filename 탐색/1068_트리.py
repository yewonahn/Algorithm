from collections import deque
import sys
input = sys.stdin.readline

# n <= 50 자연수
n = int(input())
# 부모가 없다면 (루트) -1
# 부모 노드의 번호 저장
# 노드 번호 0번 부터 시작
parent = list(map(int, input().strip().split()))
# 지울 노드의 번호
# parent 인덱스 그대로
remove = int(input())
# 삭제해야할 인덱스 저장
save = deque()
save.append(remove)


def bfs():
    global save
    # save 돌면서 삭제하고 자식 노드 있으면 저장
    # save 에는 인덱스가 아닌 노드 번호 자체 저장해야됨
    while save:
        # now = 현재 삭제할 노드 번호
        now = save.popleft()
        for a in range():

check = False
for i in range(len(parent)):
    # 같은 깊이 노드 중 부모 노드가 remove인 노드일 때까지만 반복해서 save에 저장
    if check == True and parent != remove:
        break
    elif parent[i] == remove:
        save.append(i)
        check = True

    # save 돌면서 삭제하고 자식 노드 있으면 저장
    bfs()
