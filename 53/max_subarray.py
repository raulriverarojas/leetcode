import copy
import math
class Solution:
    def maxSubArray(self, nums) -> int:
        max_val= nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(current+nums[i], nums[i])
            max_val = max(max_val, current)
        return max_val
if __name__ == '__main__':
    input = [-1,-1,-2]
    # input = [-2,1,-3,4,-1,2,1,-5,4]
    output = -1
    print("Expected out")
    print(output)
    solution = Solution()
    returned = Solution.maxSubArray(solution, input)
    print("Returned out")
    print(returned)
    assert returned == output


