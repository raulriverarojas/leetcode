from typing import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for h in range(len(triangle)-2, -1,-1):
            for i in range(len(triangle[h])):
                triangle[h][i]+=min(triangle[h+1][i], triangle[h+1][i+1])
        return triangle[0][0]

if __name__ == '__main__':
    input = [[2],[3,4],[6,5,7],[4,1,8,3]]
    output = 11
    print("Expected out")
    print(output)
    solution = Solution()
    result = Solution.minimumTotal(solution, input)
    print("Returned out")
    print(result)
    assert result == output

