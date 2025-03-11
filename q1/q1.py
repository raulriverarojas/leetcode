import copy
import math
    
class Solution:
    def findIndex(self, string)-> int:
        count = {}
        for i in range(len(string)):
            if string[i] in count:
                count[string[i]]+=1
            else:
                count[string[i]] = 1
        for k in range(len(string)):
            if count[string[k]]==1:
                return string[k]
if __name__ == '__main__':
    input = "abca"
    # input = ["2","1","+","3","*"]
    # output = 9
    output = "b"
    print("Expected out")
    print(output)
    solution = Solution()
    returned = Solution.findIndex(solution, input)
    print("Returned out")
    print(returned)
    assert returned == output

