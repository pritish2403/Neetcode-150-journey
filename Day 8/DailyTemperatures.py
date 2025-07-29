class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res

if __name__ == "__main__":
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))
