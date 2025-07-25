from typing import List

nums = [1, 2, 4, 6]
n = len(nums)
output = [1] * n

prefix = 1
for i in range(n):
    output[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n - 1, -1, -1):
    output[i] *= suffix
    suffix *= nums[i]

print(output)
