import sys
input = sys.stdin.readline

n = int(input())    # 추 개수
weights = list(map(int,input().split())) # n개의 추의 무게
m = int(input())    # 구슬 개수
target = list(map(int,input().split()))  # m개의 구슬 무게

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열 구성
dp,r = [[0 for j in range((i+1)*500+1)] for i in range(n+1)],[]

def cal(num,weight):
    # 사용할 수 있는 추의 개수를 넘어가면 종료
    if num > n:
        return 
    
    # 1. num번째까지의 추로 weight 무게를 만들 수 있음이 이미 기록되어있으면 종료
    if dp[num][weight]:
        return
    
    # 2. num번째까지 추로 weight 무게를 만들 수 있음을 체크
    dp[num][weight] = 1
    
    cal(num+1, weight)  # 추 사용하지 않음
    cal(num+1, weight+weights[num-1]) # 추의 무게 더함
    cal(num+1, abs(weight-weights[num-1]))    # 추 무게 뺌
    
cal(0,0)    # 지금까지 사용한 추 개수, 추로 만든 구슬의 무게를  0으로 시작


for i in target:
    # 만들 수 있는 구슬의 무게는 30*500이 최대
    if i > 30*500:
        r.append("N")
        continue
    if dp[n][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)
