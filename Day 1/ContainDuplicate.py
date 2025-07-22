class Solution:
    from typing import List
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 4]))
print(sol.hasDuplicate([1, 2, 3, 1]))   