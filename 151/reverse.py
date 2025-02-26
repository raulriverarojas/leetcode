import copy
class Solution:
    def reverseWords(self, s: str) -> str:
        p1=len(s)-1
        p2=len(s)-1
        result=[]
        prev=True
        for i in range(len(s)-1, -1, -1):
            if s[i]!=" ":
                if prev:
                    p2=i
                    p1=p2
                if p1==0 or s[p1-1]==" ":
                    result.append(s[p1:p2+1])
                else: 
                    p1-=1
                prev=False
            else:
                prev=True
        return " ".join(result)

if __name__ == '__main__':
    s = "a good   example"
    result="example good a"
    solution = Solution()
    returned = Solution.reverseWords(solution, s)
    print(returned)
    assert result == returned

