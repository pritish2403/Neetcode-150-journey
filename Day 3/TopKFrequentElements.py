from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        return [x for x, _ in cnt.most_common(k)]

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k)) 