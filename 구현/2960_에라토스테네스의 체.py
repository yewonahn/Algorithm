import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = [i + 2 for i in range(0, n - 1)]

cnt = 0
lst = []
while cnt != k:
    # 제일 작은 수 p
    p = nums[0]
    lst.append(p)
    nums.remove(p)
    cnt += 1
    if len(nums) == 0:
        break
    for num in nums:
        # nums[0] 의 배수 지우기
        if num % p == 0:
            cnt += 1
            lst.append(num)
            nums.remove(num)

print(lst[k-1])
