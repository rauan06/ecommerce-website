nums = [1, 2, 0]

l = len(nums)
prefix = 1
postfix = 1
answer = [0] * l

for i in range(l):
    answer[i] = prefix
    prefix *= nums[i]
for i in range(l-1,-1,-1):
    answer[i] *= postfix
    postfix *= nums[i]

print(answer)

for





