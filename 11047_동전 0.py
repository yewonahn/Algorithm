N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))


coins.reverse() # 큰 값부터 비교하기 위해서 reverse
count = 0 # 필요한 최소 동전 개수

for coin in coins:
    if K >= coin:
        count += K // coin
        K %= coin
        if K == 0:
            break

print(count)
