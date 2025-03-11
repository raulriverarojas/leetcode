from typing import *
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        index = 0
        sum_val = triangle[0][0]
        for i in range(1, len(triangle)):
            if (triangle[i][index]<triangle[i][index+1]):
                sum_val+= triangle[i][index]
            else:
                sum_val+= triangle[i][index+1]
                index+=1
        return sum_val

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

