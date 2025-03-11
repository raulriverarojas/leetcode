from typing import *
class Solution:
    def recursive(self, triangle, max_height, current_height, i):
        if current_height==max_height:
            return triangle[current_height][i]
        else:
            return triangle[current_height][i] + min(self.recursive(triangle, max_height, current_height+1, i), self.recursive(triangle, max_height, current_height+1, i+1)) 
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        max_height = len(triangle)-1
        i=0
        current_height = 0
        min_val = self.recursive(triangle, max_height, current_height, i) 
        return min_val


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

