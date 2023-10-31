import sys
input = sys.stdin.readline

H, S = map(int, input().split())

answer = []
hear = []
see = []

for _ in range(H):
    hear.append(input().rstrip())

for _ in range(S):
    see.append(input().rstrip())

hear = set(hear)
see = set(see)

answer = list(hear.intersection(see))

answer.sort()

print(len(answer))

for name in answer:
    print(name)
