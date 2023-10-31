from collections import deque

n, k = map(int, input().split())

people = deque(range(1, n + 1))
result = []

# while안에 숫자가 하나도 없기 전까지로 설정
while people:
  
  # 제거해야 하는 k번째 수를 제일 왼쪽에 두기
  for _ in range(k-1):
    people.append(people.popleft())

  result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
