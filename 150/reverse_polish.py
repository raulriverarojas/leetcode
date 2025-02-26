import copy
import math
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i]=="/":
                num2 = stack.pop()
                num1 = stack.pop()
                intermediary = num1 / num2
                intermediary = math.floor(intermediary) if intermediary>0 else math.ceil(intermediary)
                stack.append(intermediary)
            elif tokens[i]=="*":
                num2 = stack.pop()
                num1 = stack.pop()
                intermediary = num1 * num2
                stack.append(intermediary)
            elif tokens[i]=="+":
                num2 = stack.pop()
                num1 = stack.pop()
                intermediary = num1 + num2
                stack.append(intermediary)
            elif tokens[i]=="-":
                num2 = stack.pop()
                num1 = stack.pop()
                intermediary = num1 - num2
                stack.append(intermediary)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()
if __name__ == '__main__':
    input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    output = 22
    # input = ["2","1","+","3","*"]
    # output = 9
    print("Expected out")
    print(output)
    solution = Solution()
    returned = Solution.evalRPN(solution, input)
    print("Returned out")
    print(returned)
    assert returned == output

