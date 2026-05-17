class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict1 = {}
        # counter = 1
        # for num in nums:
        #     if num in dict1:
        #         return True
        #     dict1[num] = counter
        # return False
        set1 = set()
        set1add = set1.add
        for num in nums:
            if num in set1:
                return True
            set1add(num)
        return False
        
        