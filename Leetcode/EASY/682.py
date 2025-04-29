from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if op == 'C':
                ans.pop()
            elif op == 'D':
                ans.append(ans[-1] * 2)
            elif op == '+':
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(op))
        return sum(ans)

sol = Solution()
print(sol.calPoints(["5", "2", "C", "D", "+"]))  # Output: 30
