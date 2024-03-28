from itertools import combinations
import sys
input = sys.stdin.readline

# n <= 50, 0 <= k <= 26
# 단어의 개수, 가르칠 글자 수
n, k = map(int, input().strip().split())
# 8 <= len(word) <= 15
words = [list(input().strip()) for _ in range(n)]
#print(words)

# antic 제외한 문자열에서
# 글자의 순서는 상관 없음. 글자의 종류 개수만 중요
# antic 필수로 포함 되어야 하므로 k < 5 인 경우 무조건 0

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

# 글자 종류 저장
essential = ['a', 'n', 't', 'i', 'c']
alphb = set()
lst = []
index = 0
for word in words:
    save_set = set()
    save_lst = []
    for j in range(4, len(word) - 4):
        if word[j] not in essential:
            save_set.add(word[j])
            save_lst.append(word[j])

    if len(save_set) <= k - 5:
        lst.append(set())
        for i in save_lst:
            alphb.add(i)
            lst[index].add(i)
        index += 1

# print(alphb)
# print(lst)

result = 0
if len(alphb) < k-5:
    k = len(alphb) + 5
for types in combinations(alphb, k-5):
    cnt = 0
    for word in lst:
        check = True
        for now in word:
            if now not in types:
                check = False
                break
        if check:
            cnt += 1
        if cnt > result:
            result = cnt

# 학생들이 읽을 수 있는 단어 개수의 최댓값 출력
print(result)
