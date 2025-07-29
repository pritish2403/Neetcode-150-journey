class Solution:
    def generateParenthesis(self, n: int):
        res = []
        stack = [("", 0, 0)]
        while stack:
            s, open_count, close_count = stack.pop()
            if len(s) == 2 * n:
                res.append(s)
            elif open_count < n and close_count < open_count:
                stack.append((s + ")", open_count, close_count + 1))
                stack.append((s + "(", open_count + 1, close_count))
            elif open_count < n:
                stack.append((s + "(", open_count + 1, close_count))
            elif close_count < open_count:
                stack.append((s + ")", open_count, close_count + 1))
        return res

if __name__ == "__main__":
    n = 1
    sol = Solution()
    print(sol.generateParenthesis(n))
