import copy
class Solution:
    def findMinArrowShots(self, points) -> int:
        def byVal(val):
            return val[0]
        count = 0
        p1 = -float('inf')
        p2 = -float('inf')
        points.sort(key=byVal) 
        for i in range(len(points)):
            if p2>=points[i][0] and p1<=points[i][1]:
                p1 = max(p1, points[i][0])
                p2 = min(p2, points[i][1])
                continue
            else:
                count +=1
                p2 = points[i][1]
                p1 = points[i][0]
        return count 

if __name__ == '__main__':
    input = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    # input = [[10,16],[2,8],[1,6],[7,12]]
    output = 2
    print("Expected out")
    print(output)
    solution = Solution()
    returned = Solution.findMinArrowShots(solution, input)
    print("Returned out")
    print(returned)
    assert returned == output

