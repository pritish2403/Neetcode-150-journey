class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Test the function
sol = Solution()
print(sol.isAnagram("racecar", "carrace"))
print(sol.isAnagram("jar", "jam"))