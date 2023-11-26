t = int(input())

for _ in range(t) :
  n, m = input().split()
  count_1 = 0
  count_0 = 0

  for i in range(len(m)) :
    if n[i] != m[i] :
      if m[i] == '1' :
        count_1 += 1
      else :
        count_0 += 1

  print(max(count_1, count_0))
