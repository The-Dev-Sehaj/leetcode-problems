class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in myHashmap:
                return[myHashmap[difference], i]
            myHashmap[n] = i
        return
            
        