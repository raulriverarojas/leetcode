import copy
class Solution:
    def groupAnagrams(self, strs):
        map = {}
        for i in range(len(strs)):
            inner_map = tuple(0 for x in range(26))
            # inner_map={}
            for char in strs[i]:
                inner_map[ord(char)- ord('a')]+=1
            if inner_map in map:
                map[inner_map].append(strs[i])
            else:
                map[inner_map]=[strs[i]]
            # sorted_str = ''.join(sorted(strs[i]))
            # value=[]
            # if sorted_str in map:
            #     map[sorted_str].append(strs[i])
            # else:
            #     map[sorted_str]=[strs[i]]

        return list(map.values())
if __name__ == '__main__':
    input = ["eat","tea","tan","ate","nat","bat"]
    output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    print("Expected out")
    print(output)
    solution = Solution()
    returned = Solution.groupAnagrams(solution, input)
    print("Returned out")
    print(returned)
    assert returned == output

