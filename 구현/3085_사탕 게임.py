import sys
input = sys.stdin.readline

n = int(input())
# 빨 c / 파 p / 초 z / 노 y
board = [list(map(str, input().strip())) for _ in range(n)]
#print('**original board**')
#print(board)

# 먹을 수 있는 최대 개수
# 3 ≤ N ≤ 50 -> 완전 탐색

def count():
    global max
    for a in range(n):
        # cnt 0 이 아닌 1 부터 시작
        cnt = 1
        # 가로 확인
        for b in range(n-1):
            # range(n-1) 이용해서, 가로 세로 인덱스 다르게 설정
            if board[a][b] == board[a][b+1]:
                cnt += 1
            else:
                # 다음 칸에 다른 숫자 들어 있으면 초기화
                cnt = 1
            if cnt > max:
                max = cnt

        cnt = 1
        # 세로 확인
        for b in range(n - 1):
            # range(n-1) 이용해서, 가로 세로 인덱스 다르게 설정
            if board[b][a] == board[b+1][a]:
                cnt += 1
            else:
                # 다음 칸에 다른 숫자 들어 있으면 초기화
                cnt = 1
            if cnt > max:
                max = cnt


max = 0
for i in range(n):
    for j in range(n-1):
        # 가로 교환 (오른쪽)
        if j+1 < n and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            count()
            # 원상 복귀
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 세로 교환 (아래)
        if i+1 < n and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            count()
            # 원상 복귀
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(max)
